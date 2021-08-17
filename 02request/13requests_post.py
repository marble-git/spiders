# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/17
"""

import requests

data = {
    "redirect": "http://i.meishi.cc/",
    "username": "1097566154@qq.com",
    "password": "wq15290884759.",
}

if __name__ == "__main__":
    url = 'https://i.meishi.cc/login.php?redirect=http%3A%2F%2Fi.meishi.cc%2F'
    response = requests.post(url, data=data)
    print(response.text)
    pass
