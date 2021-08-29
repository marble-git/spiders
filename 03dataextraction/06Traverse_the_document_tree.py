# --coding:utf-8--
"""
@author:marble
@file:06Traverse_the_document_tree.py
@date:2021/8/29
"""

import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b>
<!--Hey, buddy. Want to buy a used parser?-->
</b>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    # print(body)
    # print(body.contents)
    # print(body.children)
    # for child in body.children:
    #     print('-'*80)
    #     print(repr(child))
    # print('descendants',body.descendants)
    # for i in body.descendants:
    #     print(repr(i))
    # print(body.child)

    p = soup.find('p', attrs={'class': 'story'})
    print(p.strings)
    # for s in p.strings:
    #     print(repr(s))

    print(p.stripped_strings)
    for s in p.stripped_strings:
        print(repr(s))

    pass
