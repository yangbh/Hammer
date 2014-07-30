##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "Ecshop" do
author "shang <s@suu.cc>" # 2014-07-07
version "0.1.2"
description "Ecshop [Chinese] - Homepage: http://www.ecshop.com/"

# Dorks #
dorks [
'"Powered By Ecshop"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
#title="Powered by ECShop" || header="ECS_ID" || body="content=\"ECSHOP" || body="/api/cron.php"
{:text=>"Powered by ECShop"},
{:text=>"content=\"ECSHOP"},
{:text=>"/api/cron.php"},
{:url=>"/js/transport.js",:text=>"ecshop"},
# Title
{:certainty=>25, :regexp=>/<title>[^<]+ - Powered by ECShop<\/title>/ },

# Version Detection # Meta Generator
{:version=>/<meta name="Generator" content="ECSHOP v([\d\.]+)" \/>/ },



]


end
