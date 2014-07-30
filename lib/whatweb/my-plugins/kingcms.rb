##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "KingCMS" do
author "shang <s@suu.cc>" # 2014-07-02
version "0.1.2"
description "KingCMS [Chinese] - Homepage: http://www.kingcms.com/"

# Dorks #
dorks [
'"Powered By KingCMS"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  
  {:text=>"<meta name=\"generator\" content=\"KingCMS\"/>"},
]


end

