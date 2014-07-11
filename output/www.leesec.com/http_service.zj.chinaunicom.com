*************************     scan info     *************************
# this is a http type scan
url:	http://service.zj.chinaunicom.com
isneighborhost:	True
*************************    scan output    *************************
>>>loading plugins
{'/root/workspace/Hammer/plugins/Info_Collect': ['neighborhost.py', 'subdomain.py', 'robots.py', 'portscan.py', 'whatweb.py'], '/root/workspace/Hammer/plugins': [], '/root/workspace/Hammer/plugins/Web_Applications': []}
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/neighborhost.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/subdomain.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/robots.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/portscan.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/whatweb.py

************************* scan services *************************
{'url': 'http://service.zj.chinaunicom.com', 'isneighborhost': True}
*************************    scan result    *************************
[{'content': {u'target': u'http://service.zj.chinaunicom.com', u'http_status': 200, u'plugins': {u'HTTPServer': {u'string': [u'nginx']}, u'Script': {u'string': [u'text/javascript']}, u'Country': {u'string': [u'CHINA'], u'module': [u'CN']}, u'Title': {u'string': [u'Redirect']}, u'nginx': {}, u'IP': {u'string': [u'220.250.64.20']}, u'Meta-Refresh-Redirect': {u'string': [u'http://nfdnserror3.wo.com.cn:8080']}}}, 'type': 'Web Application Recognition', 'level': 'info'}]
