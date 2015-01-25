

Plugin.define "Discuz" do
author "yangbh"
version "0.1"
description "discuz - homepage: http://www.discuz.net/"

# Examples #
examples %w|
www.discuz.net|

matches [

# Version detection # Powered by text
{:name=>"Powered by text",
:version=>/Powered by .*Discuz!\D*([Xx]?\d\.\d).*/},

# {:name=>"Powered by meta",
# :version=>/<meta name=\"generator\" content=\"Discuz! X([\d\.]+)\"/},

{:name=>"Powered by meta",
:version=>/<meta[^>^=]+content[\s]*=[\s]*["|']?Discuz![\s]*([Xx]?\d\.\d)(["|']?[^>^=]+name[\s]*=[\s]*["|']?generator["|']?)?/i},

{:name=>"Powered by meta",
:version=>/<meta[^>^=]+name[\s]*=[\s]*["|']?generator["|']?[^>^=]+content[\s]*=[\s]*"Discuz![\s]*([Xx]?\d\.\d)"/i},
]

end 
