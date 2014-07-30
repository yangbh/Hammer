##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "qiboSoft" do
author "shang <s@suu.cc>" # 2014-07-03
version "0.1.2"
description "qiboSoft [Chinese] - Homepage: http://www.qibosoft.com/"

# Dorks #
dorks [
'"Powered By qiboSoft"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  {:text=>"Powered by QIBOSOFT ",:version=>/V([\d\.]+)/m},
  {:url=>"/admin/template/article_more/config.htm",:text=>"qiboSoft"},
  {:url=>"/guestbook/admin/template/label/guestbook.htm",:text=>"qiboSoft"},
  
]


end
