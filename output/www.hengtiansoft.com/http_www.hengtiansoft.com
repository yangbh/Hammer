*************************     scan info     *************************
# this is a http type scan
url:	http://www.hengtiansoft.com
isneighborhost:	False
*************************    scan output    *************************
>>>loading plugins
{'/Users/mody/study/Python/Hammer/plugins/Info_Collect': ['neighborhost.py', 'portscan.py', 'robots.py', 'subdomain.py', 'whatweb.py'], '/Users/mody/study/Python/Hammer/plugins': [], '/Users/mody/study/Python/Hammer/plugins/Weak_Password': ['sshcrack.py'], '/Users/mody/study/Python/Hammer/plugins/Sensitive_Info': ['senpath.py']}
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/neighborhost.py
plugin does not run
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/portscan.py
plugin does not run
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/robots.py
plugin run
http://www.hengtiansoft.com/robots.txt
urllib2.URLError: HTTP Error 404: Not Found
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/subdomain.py
plugin does not run
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/whatweb.py
plugin run
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Weak_Password/sshcrack.py
plugin does not run
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/senpath.py

************************* scan services *************************
{'url': 'http://www.hengtiansoft.com'}
*************************    scan result    *************************
[{'content': {u'target': u'http://www.hengtiansoft.com', u'http_status': 200, u'plugins': {u'JQuery': {}, u'Cookies': {u'string': [u'.ASPXANONYMOUS', u'ASP.NET_SessionId', u'haveCount', u'lang']}, u'HTTPServer': {u'string': [u'Microsoft-IIS/6.0']}, u'ActiveX': {u'string': [u'Flash-ActiveX'], u'module': [u'D27CDB6E-AE6D-11cf-96B8-444553540000']}, u'ASP_NET': {}, u'IP': {u'string': [u'122.225.227.162']}, u'Adobe-Flash': {}, u'Script': {u'string': [u'text/javascript']}, u'X-Powered-By': {u'string': [u'ASP.NET']}, u'Object': {u'string': [u'http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0'], u'module': [u'clsid:D27CDB6E-AE6D-11cf-96B8-444553540000']}, u'Microsoft-IIS': {u'version': [u'6.0']}, u'Title': {u'string': [u'\r\n\tSoftware outsourcing, Offshore software development company in China--Insigma Hengtian Software LTD.\r\n']}, u'PasswordField': {u'string': [u'Login1$Password']}, u'HttpOnly': {u'string': [u'.ASPXANONYMOUS', u'ASP.NET_SessionId']}}}, 'type': 'Web Application Recognition', 'level': 'info'}]
