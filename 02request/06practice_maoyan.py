# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/10
"""
import urllib
from urllib import request

url = "https://piaofang.maoyan.com/dashboard-ajax?orderType=0&uuid=17b2d2a91eec8-01d1f9736c3d1b-3a7a0a5e-100200" \
      "-17b2d2a91eec8 "

# url = "https://piaofang.maoyan.com/dashboard"
# response = request.urlopen(url)
# request.urlretrieve(url,"maoyan.html")
# print(response.read())


print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 "
                  "Safari/537.36 "
}

rq = request.Request(url=url, headers=headers)
response = request.urlopen(rq)
# print(response.read().decode())
data = response.read().decode()
print(data)

import json

print(json.dumps(json.loads(data), indent=4, ensure_ascii=False))
