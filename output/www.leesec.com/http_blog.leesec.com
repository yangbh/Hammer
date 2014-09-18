*************************     scan info     *************************
# this is a http type scan
url:	http://blog.leesec.com
isneighborhost:	False

*************************   scan services   *************************

Step 1. Running Auxiliary Plugins

>>>loading plugins
{'/Users/mody/study/Python/Hammer/plugins/Weak_Password': ['sshcrack.py'], '/Users/mody/study/Python/Hammer/plugins/Common': ['fileinclusion.py'], '/Users/mody/study/Python/Hammer/plugins/Info_Collect': ['crawler.py', 'neighborhost.py', 'portscan.py', 'robots.py', 'subdomain.py', 'whatweb.py'], '/Users/mody/study/Python/Hammer/plugins/Sensitive_Info': ['backupfile.py', 'compressedfile.py', 'probefile.py', 'senpath.py'], '/Users/mody/study/Python/Hammer/plugins': [], '/Users/mody/study/Python/Hammer/plugins/System': ['dnszone.py', 'iismethod.py', 'iisshort.py', 'openssl.py', 'phpmyadmin_null_password.py', 'webdav.py'], '/Users/mody/study/Python/Hammer/plugins/Web_Applications': ['bo_blog_tag_php_xss.py', 'dedecms_downloadphp_url_redict.py', 'discuz7_2fap_php_sqlinject.py', 'discuz_x2_5_path_disclosure.py', 'espcms_search_inject.py', 'espcms_sql_inject.py', 'shopex_phpinfo_disclosure.py', 'wordpress_reflect_xss.py', 'wordpress_xmlrpc.py']}

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/crawler.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/neighborhost.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/portscan.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/robots.py
plugin run
http://blog.leesec.com/robots.txt

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/subdomain.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/whatweb.py
plugin run
cms: WordPress
cmsversion: 3.9.2
HTTPServer: nginx
X-Powered-By: PHP/5.3.28
services changed to:	{'url': 'http://blog.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}


Step 2. Running Other Plugins

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Weak_Password/sshcrack.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Common/fileinclusion.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/backupfile.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/compressedfile.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/probefile.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Sensitive_Info/senpath.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/dnszone.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/iismethod.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/iisshort.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/openssl.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/phpmyadmin_null_password.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/webdav.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/bo_blog_tag_php_xss.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/dedecms_downloadphp_url_redict.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/discuz7_2fap_php_sqlinject.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/discuz_x2_5_path_disclosure.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/espcms_search_inject.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/espcms_sql_inject.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/shopex_phpinfo_disclosure.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/wordpress_reflect_xss.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Web_Applications/wordpress_xmlrpc.py


*************************    scan result    *************************
retinfo:	[{'content': {u'HTTPServer': {u'string': [u'nginx']}, u'WordPress': {u'version': [u'3.9.2']}, u'X-Powered-By': {u'string': [u'PHP/5.3.28']}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://blog.leesec.com/.bakup\t code:200\nhttp://blog.leesec.com/.bakup\t code:200\nhttp://blog.leesec.com/.bakup\t code:200\nhttp://blog.leesec.com/.bak\t code:200\nhttp://blog.leesec.com/.bak\t code:200\nhttp://blog.leesec.com/.bak\t code:200\nhttp://blog.leesec.com/.old\t code:200\nhttp://blog.leesec.com/.bak\t code:200\nhttp://blog.leesec.com/.old\t code:200\nhttp://blog.leesec.com/.old\t code:200\nhttp://blog.leesec.com/.bakup\t code:200\nhttp://blog.leesec.com/.old\t code:200\nhttp://blog.leesec.com/wp-login.php.old\t code:200\nhttp://blog.leesec.com/wp-login.php.bakup\t code:200\nhttp://blog.leesec.com/wp-login.php.bak\t code:200\n', 'type': 'Backup Files Download Vulnerability', 'level': 'low'}, {'content': 'http://blog.leesec.com/wp-includes/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}]

services:	{'url': 'http://blog.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}