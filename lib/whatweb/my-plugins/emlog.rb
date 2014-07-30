##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "Emlog" do
author "shang <s@suu.cc>" # 2014-07-04
version "0.1.3"
description "Emlog [Chinese] - Homepage: http://www.emlog.net/"

# Dorks #
dorks [
'"Powered By Emlog"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  {:text=>"<meta name=\"generator\" content=\"emlog\" />"},
  {:text=>"Powered by <a href=\"http://www.emlog.net\" title=\"emlog "},
  {:version=>/title=\"emlog ([\d\.]+)\"/m},
  {:url=>"/robots.txt",:text=>"emlog"},
  {:url=>"/wlwmanifest.xml",:text=>"emlog"},
  {:url=>"/content/templates/default/main.css",:text=>"emlog"},
]


end

