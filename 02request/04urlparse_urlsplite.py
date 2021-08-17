# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/10
"""


from urllib import parse

url = 'http://www.baidu.com/index.html;user?id=s#comment'

result = parse.urlparse(url)
print(result)

result1 = parse.urlsplit(url)
print(result1)


