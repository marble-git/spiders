# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/17
"""

import requests

url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://221.5.80.66:3128'
}


if __name__ == "__main__":
    response = requests.get(url,proxies=proxy,timeout=5)
    print(response.text)
    pass
