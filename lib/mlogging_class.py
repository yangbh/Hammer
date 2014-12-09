# copy from https://github.com/kieslee/mlogging/blob/master/mlogging/__init__.py
# Copyright 2001-2007 by Vinay Sajip. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
Additional handler : RotatingFileHandler and TimedRotatingFileHandler 
                        for MultiProcess
"""

from logging import StreamHandler, FileHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import fcntl, time, os, codecs, string, re, types, cPickle, struct, shutil
from stat import ST_DEV, ST_INO, ST_MTIME


class StreamHandler_MP(StreamHandler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a stream. Use for multiprocess.
    """
    
    def emit(self, record):
        """
        Emit a record.
            First seek the end of file for multiprocess to log to the same file
        """
        try:
            if hasattr(self.stream, "seek"):
                self.stream.seek(0, os.SEEK_END)
        except IOError, e:
            pass
        
        StreamHandler.emit(self, record)


class FileHandler_MP(FileHandler, StreamHandler_MP):
    """
    A handler class which writes formatted logging records to disk files 
        for multiprocess
    """
    def emit(self, record):
        """
        Emit a record.

        If the stream was not opened because 'delay' was specified in the
        constructor, open it before calling the superclass's emit.
        """
        if self.stream is None:
            self.stream = self._open()
        StreamHandler_MP.emit(self, record)


class RotatingFileHandler_MP(RotatingFileHandler, FileHandler_MP):
    """
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size.
    
    Based on logging.RotatingFileHandler, modified for Multiprocess
    """
    _lock_dir = '.lock'
    if os.path.exists(_lock_dir):
        pass
    else:
        os.mkdir(_lock_dir)

    def doRollover(self):
        """
        Do a rollover, as described in __init__().
        For multiprocess, we use shutil.copy instead of rename.
        """

        self.stream.close()
        if self.backupCount > 0:
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d" % (self.baseFilename, i)
                dfn = "%s.%d" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    shutil.copy(sfn, dfn)
            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.remove(dfn)
            if os.path.exists(self.baseFilename):
                shutil.copy(self.baseFilename, dfn)
        self.mode = 'w'
        self.stream = self._open()
        
    
    def emit(self, record):
        """
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        
        For multiprocess, we use file lock. Any better method ?
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            FileLock = self._lock_dir + '/' + os.path.basename(self.baseFilename) + '.' + record.levelname
            f = open(FileLock, "w+")
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            FileHandler_MP.emit(self, record)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            f.close()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
    
        
class TimedRotatingFileHandler_MP(TimedRotatingFileHandler, FileHandler_MP):
    """
    Handler for logging to a file, rotating the log file at certain timed
    intervals.

    If backupCount is > 0, when rollover is done, no more than backupCount
    files are kept - the oldest ones are deleted.
    """
    _lock_dir = '.lock'
    if os.path.exists(_lock_dir):
        pass
    else:
        os.mkdir(_lock_dir)
    
    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=0, utc=0):
        FileHandler_MP.__init__(self, filename, 'a', encoding, delay)
        self.encoding = encoding
        self.when = string.upper(when)
        self.backupCount = backupCount
        self.utc = utc
        # Calculate the real rollover interval, which is just the number of
        # seconds between rollovers.  Also set the filename suffix used when
        # a rollover occurs.  Current 'when' events supported:
        # S - Seconds
        # M - Minutes
        # H - Hours
        # D - Days
        # midnight - roll over at midnight
        # W{0-6} - roll over on a certain day; 0 - Monday
        #
        # Case of the 'when' specifier is not important; lower or upper case
        # will work.
        if self.when == 'S':
            self.suffix = "%Y-%m-%d_%H-%M-%S"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$"
        elif self.when == 'M':
            self.suffix = "%Y-%m-%d_%H-%M"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}$"
        elif self.when == 'H':
            self.suffix = "%Y-%m-%d_%H"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}$"
        elif self.when == 'D' or self.when == 'MIDNIGHT':
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        elif self.when.startswith('W'):
            if len(self.when) != 2:
                raise ValueError("You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s" % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError("Invalid day specified for weekly rollover: %s" % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
            self.extMatch = r"^\d{4}-\d{2}-\d{2}$"
        else:
            raise ValueError("Invalid rollover interval specified: %s" % self.when)

        self.extMatch = re.compile(self.extMatch)
        
        if interval != 1:
            raise ValueError("Invalid rollover interval, must be 1")


    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        record is not used, as we are just comparing times, but it is needed so
        the method signatures are the same
        """
        if not os.path.exists(self.baseFilename):
            #print "file don't exist"  
            return 0 
        
        cTime = time.localtime(time.time()) 
        mTime = time.localtime(os.stat(self.baseFilename)[ST_MTIME])
        if self.when == "S" and cTime[5] != mTime[5]:
            #print "cTime:", cTime[5], "mTime:", mTime[5]
            return 1
        elif self.when == 'M' and cTime[4] != mTime[4]:  
            #print "cTime:", cTime[4], "mTime:", mTime[4]
            return 1  
        elif self.when == 'H' and cTime[3] != mTime[3]: 
            #print "cTime:", cTime[3], "mTime:", mTime[3]
            return 1
        elif (self.when == 'MIDNIGHT' or self.when == 'D') and cTime[2] != mTime[2]:
            #print "cTime:", cTime[2], "mTime:", mTime[2]
            return 1 
        elif self.when == 'W' and cTime[1] != mTime[1]:
            #print "cTime:", cTime[1], "mTime:", mTime[1]
            return 1
        else:  
            return 0 
    

    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        
        For multiprocess, we use shutil.copy instead of rename.
        """
        if self.stream:
            self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        #t = self.rolloverAt - self.interval
        t = int(time.time())
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        if os.path.exists(dfn):
            os.remove(dfn)
        if os.path.exists(self.baseFilename):
            shutil.copy(self.baseFilename, dfn)
            #print "%s -> %s" % (self.baseFilename, dfn)
            #os.rename(self.baseFilename, dfn)
        if self.backupCount > 0:
            # find the oldest log file and delete it
            #s = glob.glob(self.baseFilename + ".20*")
            #if len(s) > self.backupCount:
            #    s.sort()
            #    os.remove(s[0])
            for s in self.getFilesToDelete():
                os.remove(s)
        self.mode = 'w'
        self.stream = self._open()
    
    def emit(self, record):
        """
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        
        For multiprocess, we use file lock. Any better method ?
        """
        try:
            if self.shouldRollover(record):
                self.doRollover()
            FileLock = self._lock_dir + '/' + os.path.basename(self.baseFilename) + '.' + record.levelname
            f = open(FileLock, "w+")
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            FileHandler_MP.emit(self, record)
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
            f.close()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
        