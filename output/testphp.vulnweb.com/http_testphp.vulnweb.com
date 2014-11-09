*************************     scan info     *************************
# this is a http type scan
url:	http://testphp.vulnweb.com
isneighborhost:	False

*************************   scan services   *************************

Step 1. Running Auxiliary Plugins

>>>loading plugins
{'./plugins/Info_Collect': ['crawler.py', 'neighborhost.py', 'portscan.py', 'robots.py', 'subdomain.py', 'whatweb.py'], './plugins/Common': ['fileinclusion.py'], './plugins/Weak_Password': ['sshcrack.py'], './plugins/Sensitive_Info': ['backupfile.py', 'compressedfile.py', 'probefile.py', 'senpath.py'], './plugins/Web_Applications': ['bo_blog_tag_php_xss.py', 'dedecms_downloadphp_url_redict.py', 'discuz7_2fap_php_sqlinject.py', 'discuz_x2_5_path_disclosure.py', 'espcms_search_inject.py', 'espcms_sql_inject.py', 'shopex_phpinfo_disclosure.py', 'wordpress_reflect_xss.py', 'wordpress_xmlrpc.py'], './plugins': [], './plugins/System': ['dnszone.py', 'iismethod.py', 'iisshort.py', 'openssl.py', 'phpmyadmin_null_password.py', 'webdav.py']}

>>>running plugin:./plugins/Info_Collect/crawler.py
plugin run

>>>running plugin:./plugins/Info_Collect/neighborhost.py

>>>running plugin:./plugins/Info_Collect/portscan.py

>>>running plugin:./plugins/Info_Collect/robots.py
plugin run
http://testphp.vulnweb.com/robots.txt
urllib2.URLError: HTTP Error 404: Not Found

>>>running plugin:./plugins/Info_Collect/subdomain.py

>>>running plugin:./plugins/Info_Collect/whatweb.py
plugin run
HTTPServer: nginx/1.4.1
X-Powered-By: PHP/5.3.10-1~lucid+2uwsgi2
services changed to:	{'url': 'http://testphp.vulnweb.com', 'HTTPServer': u'nginx/1.4.1', 'X-Powered-By': u'PHP/5.3.10-1~lucid+2uwsgi2'}


Step 2. Running Other Plugins

>>>running plugin:./plugins/Common/fileinclusion.py

>>>running plugin:./plugins/Weak_Password/sshcrack.py

>>>running plugin:./plugins/Sensitive_Info/backupfile.py
plugin run

>>>running plugin:./plugins/Sensitive_Info/compressedfile.py
plugin run

>>>running plugin:./plugins/Sensitive_Info/probefile.py
plugin run

>>>running plugin:./plugins/Sensitive_Info/senpath.py

>>>running plugin:./plugins/Web_Applications/bo_blog_tag_php_xss.py

>>>running plugin:./plugins/Web_Applications/dedecms_downloadphp_url_redict.py

>>>running plugin:./plugins/Web_Applications/discuz7_2fap_php_sqlinject.py

>>>running plugin:./plugins/Web_Applications/discuz_x2_5_path_disclosure.py

>>>running plugin:./plugins/Web_Applications/espcms_search_inject.py

>>>running plugin:./plugins/Web_Applications/espcms_sql_inject.py

>>>running plugin:./plugins/Web_Applications/shopex_phpinfo_disclosure.py

>>>running plugin:./plugins/Web_Applications/wordpress_reflect_xss.py

>>>running plugin:./plugins/Web_Applications/wordpress_xmlrpc.py

>>>running plugin:./plugins/System/dnszone.py

>>>running plugin:./plugins/System/iismethod.py

>>>running plugin:./plugins/System/iisshort.py

>>>running plugin:./plugins/System/openssl.py

>>>running plugin:./plugins/System/phpmyadmin_null_password.py

>>>running plugin:./plugins/System/webdav.py


*************************    scan result    *************************
retinfo:	[{'content': {u'HTTPServer': {u'string': [u'nginx/1.4.1']}, u'X-Powered-By': {u'string': [u'PHP/5.3.10-1~lucid+2uwsgi2']}}, 'type': 'Web Application Recognition', 'level': 'info'}]

services:	{'url': 'http://testphp.vulnweb.com', 'HTTPServer': u'nginx/1.4.1', 'X-Powered-By': u'PHP/5.3.10-1~lucid+2uwsgi2'}