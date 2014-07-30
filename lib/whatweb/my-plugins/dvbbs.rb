##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "dvbbs" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "dvbbs [Chinese] - Homepage: http://bbs.dvbbs.net/"

# Dorks #
dorks [
'"Powered By Dvbbs"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
{:text=>"href=\"skins/dv_wnd.css",:name=>"CSS"},
{:text=>"dispuser.asp?name=",:name=>"name"},
{:text=>"dispbbs.asp?boardid=",:name=>"bbs"},
{:version=>/<a href = \"http:\/\/www.dvbbs.net\/download.asp\" target = \"_blank\">Version ([\d\.]+)/},
{:url=>"dv_rss.asp?s=xhtml",:version=>/Version ([\d\.]+)/m}
]

end
