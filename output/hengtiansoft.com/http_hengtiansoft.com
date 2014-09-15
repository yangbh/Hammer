*************************     scan info     *************************
# this is a http type scan
url:	http://hengtiansoft.com
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
http://hengtiansoft.com/robots.txt
urllib2.URLError: HTTP Error 404: Not Found

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/portscan.py

>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/whatweb.py
plugin run
HTTPServer: Microsoft-IIS/7.5
X-Powered-By: ASP.NET
services changed to:	{'url': 'http://hengtiansoft.com', 'HTTPServer': u'Microsoft-IIS/7.5', 'X-Powered-By': u'ASP.NET'}


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
plugin run
HTTP Methods found:	OPTIONS, TRACE, GET, HEAD, POST
>>>running plugin:/root/workspace/Hammer/plugins/System/dnszone.py
Vulnerable dns server found:pwsddc03.hengtiansoft.com.
Vulnerable dns server found:pwbndc02.hengtiansoft.com.
Vulnerable dns server found:pwsddc02.hengtiansoft.com.

>>>running plugin:/root/workspace/Hammer/plugins/System/openssl.py

>>>running plugin:/root/workspace/Hammer/plugins/System/iisshort.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/System/webdav.py
plugin run

>>>running plugin:/root/workspace/Hammer/plugins/System/phpmyadmin_null_password.py


*************************    scan result    *************************
retinfo:	[{'content': {u'target': u'http://hengtiansoft.com', u'http_status': 200, u'plugins': {u'HTTPServer': {u'string': [u'Microsoft-IIS/7.5']}, u'X-Powered-By': {u'string': [u'ASP.NET']}}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://hengtiansoft.com/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://hengtiansoft.com/aspnet_client/system_web/\tcode:403\nhttp://hengtiansoft.com/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://172.16.5.1:80/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://172.16.5.1:80/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://hengtiansoft.com/aspnet_client/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'OPTIONS, TRACE, GET, HEAD, POST', 'type': 'IIS PUT Vulnerability', 'level': 'info'}, {'content': 'hengtiansoft.com', 'type': 'DNS zone transfer Vulnerability', 'level': 'medium'}]

services:	{'url': 'http://hengtiansoft.com', 'HTTPServer': u'Microsoft-IIS/7.5', 'X-Powered-By': u'ASP.NET'}