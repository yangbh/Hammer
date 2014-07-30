##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "DotNetCMS" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "DotNetCMS [Chinese] - Homepage: http://www.foosun.cn/"

# Dorks #
dorks [
'"Powereds by DotNetCMS"'
]

# Matches #
matches [

{:text=>"Created by DotNetCMS"},
]

end
