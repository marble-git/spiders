# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/10
"""

from urllib import parse

data = {'name': "老wang", 'age': 18, 'greet': 'hello world', 'num': 3.14}

qs = parse.urlencode(data)
print(qs)
print(type(parse.parse_qs(qs)))

# example
from urllib import request

data1 = {'wd': '石原里美'}
qs1 = parse.urlencode(data1)
print(qs1)
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&" + qs1
print(url)
print(parse.parse_qsl(url))
response = request.urlopen(url)
print(response.read().decode())

# replenish
string = '石原里美'
print(parse.quote(string))

