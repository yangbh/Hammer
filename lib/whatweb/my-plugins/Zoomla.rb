##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "Zoomla" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "Zoomla!Cms [Chinese] - Homepage: http://www.zoomla.cn/"

# Dorks #
dorks [
'"Powereds by Zoomla!Cms"'
]

# Matches #
matches [

{:text=>"Zoomla!CMS. All Rights Reserved"},
#{:text=>"逐浪CMS</title>"},
{:text=>"ICMS/ZL_Common.js"},
{:url=>"/JS/ICMS/ZL_Common.js"},
]

end
