# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/11
"""

import urllib
import json
from urllib import request


def jsdumps(s):
    jsdata = json.loads(s)
    print(json.dumps(jsdata, indent=4))


url = "http://httpbin.org/ip"

# response = request.urlopen(url)
# jsdata = json.loads(response.read())
# print(json.dumps(jsdata,indent=4))

# jsdumps(response.read())

# use proxy
# step1: use ProxyHandler(proxies:"None/mapping"),create a handler


def get_handlers(proxies):
    result = []
    for proxy in proxies:
        handler = request.ProxyHandler(proxy)
        result.append(handler)
    return result


proxies_list = [
    {"http": "221.5.80.66:3128"},
    {"http":"124.70.46.14:3128"}
]
# handler = request.ProxyHandler({"http": "221.5.80.66:3128"})
handlers = get_handlers(proxies_list)
# step2: use created handler build an opener
opener = request.build_opener(*handlers)
# step3: use opener to send a request
response = opener.open(url, timeout=9)
jsdumps(response.read())
print('done')
# print(request.getproxies())
if __name__ == "__main__":
    pass
