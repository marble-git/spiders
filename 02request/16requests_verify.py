# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/18
"""

import requests

url = 'https://inv-veri.chinatax.gov.cn/'
if __name__ == "__main__":
    response = requests.get(url=url,verify=False)
    print(response.encoding)
    print(response.content.decode())
    pass
