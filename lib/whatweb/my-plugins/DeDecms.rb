##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "DeDeCms" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "DeDeCms [Chinese] - Homepage: http://www.dedecms.com/"

# Dorks #
dorks [
'"Powereds by DedeCms"'
]

# Matches #
matches [

{:text=>"Q Q "},#这是那个龙少什么的做的黑站，都是dede  
{:text=>"<a target=\"_blank\" href=\"http://www.dedecms.com/"},
{:text=>"/templets/default/style/dedecms.css",:name=>"CSS File"},
{:text=>"http://www.dedecms.com/baodiao/diaoyudao.js"},
{:text=>"/include/dedeajax2.js"},
{:text=>"Power by DedeCms"},
{:url=>"/templets/default/style/dedecms.css",:version=>/DedeCMS v([\d\.]+)/m},

]


end
