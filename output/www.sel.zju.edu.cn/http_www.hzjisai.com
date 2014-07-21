*************************     scan info     *************************
# this is a http type scan
url:	http://www.hzjisai.com
isneighborhost:	True
*************************    scan output    *************************
>>>loading plugins
{'/root/workspace/Hammer/plugins/Sensitive_Info': ['senpath.py'], '/root/workspace/Hammer/plugins/Info_Collect': ['neighborhost.py', 'subdomain.py', 'spider.py', 'robots.py', 'portscan.py', 'whatweb.py'], '/root/workspace/Hammer/plugins': [], '/root/workspace/Hammer/plugins/Weak_Password': ['sshcrack.py'], '/root/workspace/Hammer/plugins/Web_Applications': []}
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/neighborhost.py
plugin does not run
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/subdomain.py
plugin does not run
>>>running plugin:/root/workspace/Hammer/plugins/Info_Collect/spider.py

************************* scan services *************************
{'url': 'http://www.hzjisai.com', 'isneighborhost': True}
*************************    scan result    *************************
[]
