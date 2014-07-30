##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "PHP168" do
author "shang <s@suu.cc>" # 2014-07-07
version "0.1.3"
description "PHP168 [Chinese] - Homepage: http://www.php168.net/"

# Dorks #
dorks [
'"Powered by PHP168.com"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
   {:text=>"/php168/"},
   {:text=>"Powered By www.php168.com"},
   {:text=>"Powered by <a href=\"http:\/\/www.php168.com\" target=\"_blank\">PHP168"},
   {:version=>/PHP168 V([\d\.]+)<\/a>/m},
   {:text=>"<a href=\"http:\/\/www.php168.com\/bbs\" target=\"_blank\">PHP168cms</a>"},
   {:url=>"/admin/",:text=>"PHP168"}
]



end
