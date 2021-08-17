# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/10
"""


from urllib import request


url = "http://www.baidu.com"
headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

rq = request.Request(url=url,headers=headers)
response = request.urlopen(url)
print(rq)
print(response)
print(response.read(100))