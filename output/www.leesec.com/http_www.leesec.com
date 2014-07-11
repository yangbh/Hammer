*************************     scan info     *************************
# this is a http type scan
url:	http://www.leesec.com
isneighborhost:	False
*************************    scan output    *************************
>>>loading plugins
{'/root/workspace/Hammer/plugins/Info_Collect': ['neighborhost.py', 'subdomain.py', 'robots.py', 'portscan.py', 'whatweb.py'], '/root/workspace/Hammer/plugins': [], '/root/workspace/Hammer/plugins/Web_Applications': []}
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/neighborhost.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/subdomain.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/robots.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/portscan.py
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/whatweb.py

************************* scan services *************************
{'url': 'http://www.leesec.com', 'cms': 'WordPress', 'cmsversion': [u'3.9.1']}
*************************    scan result    *************************
[{'content': 'User-agent: *\nDisallow: /wp-admin/\nDisallow: /wp-includes/\n', 'type': 'Robots.txt Sensitive Information', 'level': 'info'}, {'content': {u'target': u'http://www.leesec.com', u'http_status': 200, u'plugins': {u'JQuery': {u'version': [u'1.11.0']}, u'Adobe-Flash': {}, u'HTTPServer': {u'string': [u'nginx']}, u'X-Powered-By': {u'string': [u'PHP/5.3.28']}, u'Country': {u'string': [u'JAPAN'], u'module': [u'JP']}, u'UncommonHeaders': {u'string': [u'x-pingback']}, u'MetaGenerator': {u'string': [u'WordPress 3.9.1']}, u'WordPress': {u'version': [u'3.9.1']}, u'HTML5': {}, u'nginx': {}, u'IP': {u'string': [u'106.187.37.47']}, u'Title': {u'string': [u'Leesec&#039;s Blog | \u4e13\u6ce8\u7f51\u7edc\u5b89\u5168\u3001\u7f16\u7a0b']}, u'PHP': {u'version': [u'5.3.28']}, u'Script': {u'string': [u'text/javascript']}, u'Email': {u'string': [u'geoff@deconcept.com']}, u'x-pingback': {u'string': [u'http://www.leesec.com/xmlrpc.php']}}}, 'type': 'Web Application Recognition', 'level': 'info'}]
