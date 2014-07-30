##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "PHPWind" do
author "shang <s@suu.cc>" # 2014-07-07
version "0.1.2"
description "PHPWind [Chinese] - Homepage: http://www.phpwind.net/"

# Dorks #
dorks [
'"Powered by phpwind"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  
  {:text=>"js/pw_ajax.js"},
  {:url=>"js/pw_ajax.js"},
  {:version=>/<meta name=\"generator\" content=\"phpwind v([\d\.]+\([\d\.]+\))\"/m},
  {:url=>"/bbs/",:version=>/<meta name=\"generator\" content=\"phpwind v([\d\.]+\([\d\.]+\))\"/m},
  {:version=>/>phpwind v([\d\.]+)<\/a>/m}
  
]


end
