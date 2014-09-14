*************************     scan info     *************************
# this is a http type scan
url:	http://www.hengtiansoft.com
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
http://www.hengtiansoft.com/robots.txt

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/subdomain.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/Info_Collect/whatweb.py
plugin run
HTTPServer: Microsoft-IIS/6.0
X-Powered-By: ASP.NET
services changed to:	{'url': 'http://www.hengtiansoft.com', 'HTTPServer': u'Microsoft-IIS/6.0', 'X-Powered-By': u'ASP.NET'}


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
plugin run
HTTP Methods found:	OPTIONS, TRACE, GET, HEAD
>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/iisshort.py
plugin run

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/openssl.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/phpmyadmin_null_password.py

>>>running plugin:/Users/mody/study/Python/Hammer/plugins/System/webdav.py
plugin run

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
retinfo:	[{'content': {u'target': u'http://www.hengtiansoft.com', u'http_status': 200, u'plugins': {u'HTTPServer': {u'string': [u'Microsoft-IIS/6.0']}, u'X-Powered-By': {u'string': [u'ASP.NET']}}}, 'type': 'Web Application Recognition', 'level': 'info'}, {'content': 'http://www.hengtiansoft.com/aspnet_client/\tcode:403\nhttp://www.hengtiansoft.com/images/\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/2_0_50727/\tcode:403\nhttp://www.hengtiansoft.com/images\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/FreeTextBox/\tcode:403\nhttp://www.hengtiansoft.com/upload\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/2_0_50727\tcode:403\nhttp://www.hengtiansoft.com/aspnet_client/system_web/\tcode:403\n', 'type': 'Sensitive File/Directory Discover', 'level': 'low'}, {'content': 'OPTIONS, TRACE, GET, HEAD', 'type': 'IIS PUT Vulnerability', 'level': 'info'}]

services:	{'url': 'http://www.hengtiansoft.com', 'HTTPServer': u'Microsoft-IIS/6.0', 'X-Powered-By': u'ASP.NET'}