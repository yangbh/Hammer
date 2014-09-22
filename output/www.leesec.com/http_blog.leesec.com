*************************     scan info     *************************
# this is a http type scan
url:	http://blog.leesec.com
isneighborhost:	False

*************************   scan services   *************************

Step 1. Running Auxiliary Plugins

>>>loading plugins
{'/root/workspace/Hammer/plugins/Info_Collect': ['neighborhost.py', 'subdomain.py', 'crawler.py', 'robots.py', 'portscan.py', 'whatweb.py'], '/root/workspace/Hammer/plugins/Weak_Password': ['sshcrack.py'], '/root/workspace/Hammer/plugins/Sensitive_Info': ['backupfile.py', 'compressedfile.py', 'senpath.py', 'probefile.py'], '/root/workspace/Hammer/plugins/Common': ['fileinclusion.py'], '/root/workspace/Hammer/plugins': [], '/root/workspace/Hammer/plugins/Web_Applications': ['espcms_search_inject.py', 'discuz_x2_5_path_disclosure.py', 'shopex_phpinfo_disclosure.py', 'dedecms_downloadphp_url_redict.py', 'discuz7_2fap_php_sqlinject.py', 'bo_blog_tag_php_xss.py', 'wordpress_reflect_xss.py', 'espcms_sql_inject.py', 'wordpress_xmlrpc.py'], '/root/workspace/Hammer/plugins/System': ['iismethod.py', 'dnszone.py', 'openssl.py', 'iisshort.py', 'webdav.py', 'phpmyadmin_null_password.py']}

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/neighborhost.py

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/subdomain.py

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/crawler.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/robots.py
plugin run
http://blog.leesec.com/robots.txt

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/portscan.py

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/whatweb.py
plugin run
cms: WordPress
cmsversion: 3.9.2
HTTPServer: nginx
X-Powered-By: PHP/5.3.28
services changed to:	{'url': 'http://blog.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}


Step 2. Running Other Plugins

>>>running plugin:/root/workspace/Hammer/plugins/Weak_Password/sshcrack.py

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/backupfile.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/compressedfile.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/senpath.py

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/probefile.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Common/fileinclusion.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/espcms_search_inject.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/discuz_x2_5_path_disclosure.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/shopex_phpinfo_disclosure.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/dedecms_downloadphp_url_redict.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/discuz7_2fap_php_sqlinject.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/bo_blog_tag_php_xss.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/wordpress_reflect_xss.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/espcms_sql_inject.py

>>>running plugin:/root/workspace/Hammer/plugins/Web_Applications/wordpress_xmlrpc.py

>>>running plugin:/root/workspace/Hammer/plugins/System/iismethod.py

>>>running plugin:/root/workspace/Hammer/plugins/System/dnszone.py

>>>running plugin:/root/workspace/Hammer/plugins/System/openssl.py

>>>running plugin:/root/workspace/Hammer/plugins/System/iisshort.py

>>>running plugin:/root/workspace/Hammer/plugins/System/webdav.py

>>>running plugin:/root/workspace/Hammer/plugins/System/phpmyadmin_null_password.py


*************************    scan result    *************************
retinfo:	[{'content': {u'HTTPServer': {u'string': [u'nginx']}, u'WordPress': {u'version': [u'3.9.2']}, u'X-Powered-By': {u'string': [u'PHP/5.3.28']}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://blog.leesec.com/.bak\t code:200\nhttp://blog.leesec.com/.bakup\t code:200\nhttp://blog.leesec.com/wp-login.php.old\t code:200\nhttp://blog.leesec.com/.old\t code:200\nhttp://blog.leesec.com/wp-login.php.bak\t code:200\nhttp://blog.leesec.com/wp-login.php.bakup\t code:200\n', 'type': 'Backup Files Download Vulnerability', 'level': 'low'}, {'content': 'http://blog.leesec.com/blog.leesec.com.tar.gz\tcode:200\nhttp://blog.leesec.com/1.tar\tcode:200\nhttp://blog.leesec.com/1.tar.gz\tcode:200\nhttp://blog.leesec.com/blog.leesec.com.rar\tcode:200\nhttp://blog.leesec.com/blog.leesec.com.tar\tcode:200\nhttp://blog.leesec.com/1.zip\tcode:200\nhttp://blog.leesec.com/1.rar\tcode:200\nhttp://blog.leesec.com/leesec.com.rar\tcode:200\nhttp://blog.leesec.com/blog.leesec.com.zip\tcode:200\nhttp://blog.leesec.com/leesec.com.tar\tcode:200\nhttp://blog.leesec.com/wp-admin/1.tar\tcode:200\nhttp://blog.leesec.com/leesec.com.tar.gz\tcode:200\nhttp://blog.leesec.com/wp-admin/1.rar\tcode:200\nhttp://blog.leesec.com/wp-admin/1.tar.gz\tcode:200\nhttp://blog.leesec.com/wp-admin/wp-admin.zip\tcode:200\nhttp://blog.leesec.com/wp-admin/wp-admin.tar.gz\tcode:200\nhttp://blog.leesec.com/leesec.com.zip\tcode:200\nhttp://blog.leesec.com/wp-admin/wp-admin.rar\tcode:200\nhttp://blog.leesec.com/wp-admin/1.zip\tcode:200\nhttp://blog.leesec.com/wp-admin/wp-admin.tar\tcode:200\nhttp://blog.leesec.com/wp-admin/www.tar\tcode:200\nhttp://blog.leesec.com/www.tar\tcode:200\nhttp://blog.leesec.com/www.zip\tcode:200\nhttp://blog.leesec.com/www.rar\tcode:200\nhttp://blog.leesec.com/wp-admin/www.zip\tcode:200\nhttp://blog.leesec.com/www.tar.gz\tcode:200\nhttp://blog.leesec.com/wp-admin/www.rar\tcode:200\nhttp://blog.leesec.com/wp-admin/www.tar.gz\tcode:200\n', 'type': 'Compresed Files Download Vulnerability', 'level': 'medium'}]

services:	{'url': 'http://blog.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}