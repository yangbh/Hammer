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

# Dorks #
dorks [
'"Powered By EspCMS"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200

  {:url=>"/license.txt",:text=>"espcms"},
  {:text=>"espcms"},
  {:url=>"/templates/wap/cn/public/footer.html",:text=>"espcms"},
]



end
