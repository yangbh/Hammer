##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "Hikvision" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "Hikvision  - Homepage: http://www.hikvision.com/"

# Dorks #
dorks [
'"Powereds by Hikvision"'
]

# Matches #
matches [

{:url=>"/doc/page/login.asp",:text=>"Hikvision Digital Technology"},
#{:text=>"Hikvision Digital Technology"},
{:text=>"doc/page/login.asp"}
]

end
