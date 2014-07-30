##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "EmpireCMS" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "Open source CMS - homepage: http://www.phome.net/"

# Dorks #
dorks [
'"Powered by EmpireCMS"'
]



matches [

{:text=>"Powered by EmpireCMS"},
{:text=>"/e/member/login/loginjs.php"},
{:text=>"href=\"#ecms",:name=>"Tag"},
{:text=>"EmpireSoft Inc.</a>",:name=>"EmpireSoft Inc."},
{:version=>/<font color=\"#FF9900\">([\d\.]+)/},

]


end

