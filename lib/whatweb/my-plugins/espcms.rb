##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "EspCMS" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "EspCMS [Chinese] - Homepage: http://www.ecisp.cn/"
examples %w| www.maris-reg.com xmhuixinda.com  www.data-express.cn www.tycomputer.com www.lokfly.com|

# Dorks #
dorks [
'"Powered By EspCMS"'
]

# Matches #
matches [
	{:name=>"file license.txt",:url=>"/license.txt",:text=>"espcms"},
	{:text=>"ESPCMS"},
	{:filepath=>"/templates/wap/cn/public/footer.html",:text=>"ESPCMS"},
	# {:filepath=>"/api/uc.php",:md5=>"f4c65c2e278282b8f614f6bdc086e4a8"},
	# {:filepath=>"/js/My97DatePicker/lang/en.js",:md5=>"0132b0df672d053d320458a937450b65"},
	# {:filepath=>"/js/My97DatePicker/lang/en.js",:md5=>"71ed96d7a61bf1f078eadeaae518ab9c"},
]

end
