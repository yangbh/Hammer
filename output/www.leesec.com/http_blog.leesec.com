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

