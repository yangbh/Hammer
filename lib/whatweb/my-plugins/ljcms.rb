##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "LjCMS" do
author "shang <s@suu.cc>" # 2014-07-02
version "0.1.2"
description "LjCMS [Chinese] - Homepage: http://www.liangjing.org/"

# Dorks #
dorks [
'"Powered By LjCMS"'
]

# Matches #
matches [

  # url exists, i.e. returns HTTP status 200
  #// 本代码由LJcms(良精内容管理系统)整理优化
  #// 如果还需要增加图片，请copy上面的代码即可
  #// 如果还需要增加图片，请copy上面的代码即可
  #// 如果还需要增加图片，请copy上面的代码即可
  #// 显示幻灯片式的网页图片滚动
  #document.write(roll_pic_flash(roll_pic_ary));
  #// 如果要嵌入其他系统内（如cms），稍做修改即可使用
  {:text=>"LJcms("},
  

]


end
