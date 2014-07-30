##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "AWStats" do
author "shang <s@suu.cc>" # 2014-07-09
version "0.1.2"
description "AWStats is a free powerful and featureful tool that generates advanced web, streaming, ftp or mail server statistics, graphically.  - Homepage: http://awstats.sourceforge.net/"

# Dorks #
dorks [
'"Powereds by AWStats"'
]

# Matches #
matches [

{:url=>"/awstats/awstats.pl?config=wellness",:version=>/<meta name=\"generator\" content=\"AWStats ([\d\.]+ \(build [\d\.]+\) )/m},
{:url=>"/cgi-bin/awstats/awstats.pl?config=wellness",:version=>/<meta name=\"generator\" content=\"AWStats ([\d\.]+ \(build [\d\.]+\) )/m},
]

end
