# --coding:utf-8--
"""
@author:marble
@file:05BeautifulSoup的4个常用对象.py
@date:2021/8/26
"""

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<b><!--Hey, buddy. Want to buy a used parser?--></b>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


from bs4 import BeautifulSoup
if __name__ == '__main__':
    soup = BeautifulSoup(html,'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.a)
    from bs4.element import Tag

    print(soup.title.string)
    print(type(soup.title.string))
    from bs4.element import NavigableString

    print(type(soup))

    from bs4.element import Comment
    print(soup.b.string)
    print(type(soup.b.string))
