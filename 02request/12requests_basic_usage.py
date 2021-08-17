# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/16
"""

import urllib
from urllib import request
from urllib import parse
import requests

url = "https://www.baidu.com/s?"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

data = {
    "wd": '中国'
}

print('-'*50)
# rq = request.Request(url+parse.urlencode(data),headers=headers)
# resp1 = request.urlopen(rq)
# print(resp1)
# # print(resp1.read().decode())

print('-'*50)

resp2 = requests.get(url=url, params=data,headers=headers)
print(type(resp2))
print(resp2.encoding)
print(resp2.text)
# print(resp2.content.decode())
print(resp2.url)



if __name__ == "__main__":
    pass
