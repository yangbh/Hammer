##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "FoosunCMS" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "FoosunCMS [Chinese] - Homepage: http://www.foosun.cn/"

# Dorks #
dorks [
'"Powered By FoosunCMS"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  
{:text=>"For Foosun"},
{:text=>"FS/"},
{:text=>"by Foosun.Cn,Foosun Content Management System"},
{:version=>/([\d\.]+)\(FoosunCMS\)/m},
{:text=>"FS_Inc/Prototype.js"},
{:url=>"/Tags.html",:text=>"By Foosun.Cn"},

]


end
