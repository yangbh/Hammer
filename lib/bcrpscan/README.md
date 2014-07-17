bcrpscan
========

Base on crawler result web path scanner.

For a url which is a directory: http://test.com/a/, it will try to get:

```
http://test.com/a.zip
http://test.com/a.rar
http://test.com/a.tar.gz
...
```

For a url which is a file: http://test.com/b.php, it will try to get:

```
http://test.com/b.php.bak
http://test.com/b.php.1
...
```

Install
========

- Need: Python2.7

Usage
========

```
bcrpscan.py (-i import_url_list_file | -u url) [-c cookie_file] [-d db_path] [-h]
```

Example
========

```
$ python bcrpscan.py -i test_urls
2014-04-20 19:43:03,484  INFO: http://192.168.1.6/test
2014-04-20 19:43:13,625  INFO: http://192.168.1.6/test67187c0f
2014-04-20 19:43:13,632  INFO: http://192.168.1.6/test.tar.gz
2014-04-20 19:43:13,638  INFO: http://192.168.1.6/test.zip
2014-04-20 19:43:13,646  INFO: http://192.168.1.6/test.rar
2014-04-20 19:43:13,733  INFO: http://192.168.1.667187c0f
2014-04-20 19:43:13,862  INFO: http://192.168.1.6/test.tar.bz2
2014-04-20 19:43:13,867  INFO: [+] http://192.168.1.6/test.rar
2014-04-20 19:43:23,847  INFO: http://192.168.1.6/test.rar250

------------------------------
Probed web paths:
http://192.168.1.6/test.rar
```

Copyright (c) 2014 secfree, released under the GPL license
