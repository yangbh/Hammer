crawler
=======

#### A Web crawler.  
* Start from the url and crawl the web pages with a specified depth.  
* Save the pages which contain a keyword(if provided) into database.  
* Support multi-threading.  
* Support logging.  
* Support self-testing.  



usage
-------------
```shell
main.py [-h] -u URL -d DEPTH [--logfile FILE] [--loglevel {1,2,3,4,5}]
               [--thread NUM] [--dbfile FILE] [--key KEYWORD] [--testself]
```

optional arguments:
-------------
```shell
  -h, --help            show this help message and exit
  -u URL                Specify the begin url
  -d DEPTH              Specify the crawling depth
  --logfile FILE        The log file path, Default: spider.log
  --loglevel {1,2,3,4,5}
                        The level of logging details. Larger number record
                        more details. Default:3
  --thread NUM          The amount of threads. Default:10
  --dbfile FILE         The SQLite file path. Default:data.sql
  --key KEYWORD         The keyword for crawling. Default: None. For more then
                        one word, quote them. example: --key 'Hello world'
  --testself            Crawler self test

```