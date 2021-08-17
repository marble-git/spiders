# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/11
    l = "http://www.biedoul.com"
"""

from urllib import request
from urllib import parse

#
url = "http://www.biedoul.com"


#
# response = request.urlopen(url)
# print(response.read().decde())


def get1page(url, path):
    target = parse.urljoin(url, path)
    print(target)
    response = request.urlopen(target)
    return response


# page = get1page(url, "index/14233")
# print(page.read().decode("utf-8"))

if __name__ == "__main__":
    for num in range(14233,14243):
        path = "index/"+str(num)
        page = get1page(url, path)
        print(page.read(100).decode("utf-8"))