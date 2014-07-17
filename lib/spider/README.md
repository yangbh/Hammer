second-spider
=============

A simple python gevent concurrency spider

### Features

1. The concurrency foundation on [gevent](http://www.gevent.org/)
2. The spider strategy highly configurable:

> 
* Max depth 
* Sum totals of urls
* Max concurrency of http request,avoid dos
* Request headers and cookies
* Same host strategy
* Same domain strategy
* Max running time


### Dependencies

* python 2.7  
* ~~* gevent 1.0dev~~
* [gevent 1.0 final](https://github.com/surfly/gevent/releases/tag/1.0)
* requests 1.0.3
* pyquery 1.2.4


### Test

```
python spider.py -v
```

### Example

```
import logging
from spider  import Spider

logging.basicConfig(
        level=logging.DEBUG ,
        format='%(asctime)s %(levelname)s %(message)s')

spider = Spider()
spider.setRootUrl("http://www.sina.com.cn")
spider.run()

```


### TODO

* Support Distributed , update `gevent.Queue` -> `redis.Queue`
* Storage backend highly configurable
* Support Ajax url (webkit etc..)


### LICENSE

Copyright © 2013 by kenshin

Under MIT license : [rem.mit-license.org](http://rem.mit-license.org/)


