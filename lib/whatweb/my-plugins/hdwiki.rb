##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "HdWiki" do
author "shang <s@suu.cc>" # 2014-06-30
version "0.1.1"
description "HdWiki [Chinese] - Homepage: http://kaiyuan.hudong.com/"

# Dorks #
dorks [
'"Powered By HdWiki"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  #header="hd_sid="
   {:text=>"powered by hdwiki!"},
   {:text=>"content=\"HDWiki"},
   {:text=>"http://kaiyuan.hudong.com?hf=hdwiki_copyright_kaiyuan"},
   {:text=>"hdwiki.css"},
   {:url=>"/robots.txt",:text=>"hdwiki"},
   {:url=>"/js/api.js",:text=>"hdwiki"},
 ]


end
