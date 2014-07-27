*************************     scan info     *************************
# this is a http type scan
url:	https://canju.hengtiansoft.com
isneighborhost:	False

*************************   scan services   *************************

Step 1. Running Auxiliary Plugins

>>>loading plugins
{'/Users/mody/study/Python/Hammer/plugins/Info_Collect': ['crawler.py', 'neighborhost.py', 'portscan.py', 'robots.py', 'subdomain.py', 'whatweb.py'], '/Users/mody/study/Python/Hammer/plugins': [], '/Users/mody/study/Python/Hammer/plugins/Weak_Password': ['sshcrack.py'], '/Users/mody/study/Python/Hammer/plugins/Sensitive_Info': ['senpath.py']}

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/crawler.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/neighborhost.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/portscan.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/robots.py
plugin run
https://canju.hengtiansoft.com/robots.txt
urllib2.URLError: HTTP Error 404: Not Found

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/subdomain.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/whatweb.py
plugin run


Step 2. Running Other Plugins

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Weak_Password/sshcrack.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/senpath.py


*************************    scan result    *************************
retinfo:	[{'content': {u'target': u'https://canju.hengtiansoft.com', u'http_status': 200, u'plugins': {u'Title': {u'string': [u'Welcome to nginx!']}, u'IP': {u'string': [u'124.160.91.84']}, u'HTTPServer': {u'string': [u'nginx/1.2.1']}, u'nginx': {u'version': [u'1.2.1']}}}, 'type': 'Web Application Recognition', 'level': 'info'}]

services:	{'url': 'https://canju.hengtiansoft.com'}