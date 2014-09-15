*************************     scan info     *************************
# this is a http type scan
url:	http://www.leesec.com
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
http://www.leesec.com/robots.txt

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/portscan.py

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/whatweb.py
plugin run
cms: WordPress
cmsversion: 3.9.2
HTTPServer: nginx
X-Powered-By: PHP/5.3.28
services changed to:	{'url': 'http://www.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}


Step 2. Running Other Plugins

>>>running plugin:/root/workspace/Hammer/plugins/Weak_Password/sshcrack.py

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/backupfile.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/compressedfile.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/Sensitive_Info/senpath.py
plugin run

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
retinfo:	[{'content': 'User-agent: *\nDisallow: /wp-admin/\nDisallow: /wp-includes/\n', 'type': 'Robots.txt Sensitive Information', 'level': 'info'}, {'content': {u'target': u'http://www.leesec.com', u'http_status': 200, u'plugins': {u'HTTPServer': {u'string': [u'nginx']}, u'WordPress': {u'version': [u'3.9.2']}, u'X-Powered-By': {u'string': [u'PHP/5.3.28']}}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://www.leesec.com/wp-includes/\tcode:403\nhttp://www.leesec.com/uploads/include/dialog/select_soft_post.php\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'http://www.leesec.com/wp-content/uploads/phpinfo.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/test.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/1.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/php.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/info.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/phpinfo.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/1.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/info.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/test.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/php.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/04/test.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/04/phpinfo.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/04/1.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/04/info.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2014/04/php.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/1.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/phpinfo.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/info.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/test.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/php.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/10/phpinfo.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/10/test.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/10/1.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/10/php.php\t code:403\nhttp://www.leesec.com/wp-content/uploads/2013/10/info.php\t code:403\n', 'type': 'Probe File Discover', 'level': 'low'}]

services:	{'url': 'http://www.leesec.com', 'HTTPServer': u'nginx', 'cms': 'WordPress', 'X-Powered-By': u'PHP/5.3.28', 'cmsversion': u'3.9.2'}