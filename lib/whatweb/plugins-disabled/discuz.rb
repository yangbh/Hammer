##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "discuz" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "Discuz! [Chinese] - Homepage: http://www.discuz.net/"

# Dorks #
dorks [
'"Powered by Discuz!"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
{:text=>"<meta name=\"generator\" content=\"Discuz! X",
:name=>"Generator"},
{:text=>"<meta name=\"author\" content=\"Discuz! Team and Comsenz UI Team\" />",
:name=>"Author"},
{:text=>"discuz_uid",
:name=>"UID"},
{:version=>/<meta name=\"generator\" content=\"Discuz! X([\d\.]+)\"/},
{:url=>"/robots.txt",
:text=>"Discuz! X"}

]

end
