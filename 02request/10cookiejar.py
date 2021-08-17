# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/13
    # 登录：https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F
#个人网页https://i.meishi.cc/cook.php?id=13686422
"""

import urllib
import re
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
# 1 login
# 1.1 create cookiejar object
cj = CookieJar()
for i in cj:
    print("cji0:",i)
# 1.2 create handler(request.HTTPCookieProcessor obj) with cj object
handler = request.HTTPCookieProcessor(cj)
# 1.3 create opener(request.build_opener) with handler
opener = request.build_opener(handler)
# 1.4 use opener to send post login request.
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
post_data = parse.urlencode({
    'username':'1097566154@qq.com',
    'password':'wq15290884759.'
}).encode('utf8')

rq = request.Request(url=post_url, data=post_data,headers=headers)
response = opener.open(rq)


# 2.访问个人网页
url = 'https://i.meishi.cc/cook.php?id=13686422'
req = request.Request(url,headers=headers)
# resp = request.urlopen(req)   #no login
resp = opener.open(req)         #login
# print(resp.read().decode('utf-8'))

for i in cj:
    print('cj i:',i)

if __name__ == "__main__":
    # print('cj:', dir(cj))
    # print("handler:", handler.cookiejar)
    # print('opener:', dir(opener))
    pass
