*************************     scan info     *************************
# this is a http type scan
url:	http://canju.hengtiansoft.com
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
http://canju.hengtiansoft.com/robots.txt

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/subdomain.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/whatweb.py
plugin run
cms: WordPress
services changed to:	{'url': 'http://canju.hengtiansoft.com', 'cms': 'WordPress'}


Step 2. Running Other Plugins

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Weak_Password/sshcrack.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/senpath.py


*************************    scan result    *************************
retinfo:	[{'content': {u'target': u'http://canju.hengtiansoft.com', u'http_status': 200, u'plugins': {u'X-UA-Compatible': {u'string': [u'IE=edge']}, u'HTTPServer': {u'string': [u'Apache-Coyote/1.1']}, u'Script': {}, u'IP': {u'string': [u'124.160.91.84']}, u'Title': {u'string': [u'\u9910\u805a']}, u'WordPress': {u'certainty': 75}, u'HTML5': {}, u'Apache': {}, u'Email': {u'string': [u'mobile@hengtiansoft.com']}, u'All-in-one-SEO-Pack': {u'version': [u'1.6.15.3']}}}, 'type': 'Web Application Recognition', 'level': 'info'}]

services:	{'url': 'http://canju.hengtiansoft.com', 'cms': 'WordPress'}