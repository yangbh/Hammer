##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "SiteServer" do
author "shang <s@suu.cc>" # 2014-07-02
version "0.1.2"
description "SiteServer [Chinese] - Homepage: http://www.siteserver.cn/"

# Dorks #
dorks [
'"Powered By SiteServer"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  {:text=>"Powered by SiteServer CMS"},
  {:url=>"/robots.txt",:text=>"SiteServer"},
  {:url=>"/UserCenter/Inc/script.js",:text=>"siteserver"},
#  {:search=>"headers[set-cookie]",:regexp=>/SITESERVER=ID=[0-9a-z]{32};/ },
  
]

# Passive #
def passive
	m=[]

	# X-Powered-By Headers
	m << {:name=>"SiteServer Cookie" } if @headers["set-cookie"] =~ /SITESERVER=ID=[0-9a-z]{32}/

	# Return passive matches
	m
end


end
