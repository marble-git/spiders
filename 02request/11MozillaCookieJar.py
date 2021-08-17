# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/16
    ignore_discard
    ignore_expires
"""

import urllib
from urllib import request
from http.cookiejar import MozillaCookieJar

# url = "https://www.baidu.com"
url = "http://httpbin.org/cookies/set/cjname/cjvalue"
if __name__ == "__main__":
    cj = MozillaCookieJar('cookie.txt')
    # handler = request.HTTPCookieProcessor(cj)
    # opener = request.build_opener(handler)
    # response = opener.open(url)
    # for i in cj:
    #     print('i0', i)
    # cj.save(ignore_discard=True, ignore_expires=True)

    cj.load(ignore_discard=True, ignore_expires=True)
    for i in cj:
        print('i1', i)
    pass
