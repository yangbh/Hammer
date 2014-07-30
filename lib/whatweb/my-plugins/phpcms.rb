##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "phpCMS" do
author "shang <s@suu.cc>" # 2014-07-02
version "0.1.1"
description "phpCMS [Chinese] - Homepage: http://www.phpcms.cn/"

# Dorks #
dorks [
'"Powered By phpCMS"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200

  {:text=>"phpcms"},
  {:text=>"<meta name=\"phpCMS.robots"},
  {:text=>"<!-- PHPCMS_NOINDEX"},
  
]


end
