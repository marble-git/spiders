# --coding:utf-8--
"""
@author:marble
@file:08select.py
@date:2021/8/31
"""
import re

import bs4
from bs4 import BeautifulSoup
from pprint import pprint

html = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>
<img src='http://baidu.com' id='link2'>
<p class="story">Once upon a time there were three little sisters; and their names were
<a title='t1' href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a title='t-2 td' href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a title='t-3' href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
<a href='test.org'> test something </a>
"""
if __name__ == '__main__':
    soup = BeautifulSoup(html,'lxml')
    # pprint(soup)
    # （1）通过标签名查找：
    print(sel:=soup.select('a'),type(sel))
    # （2）通过类名查找：
    # pprint(soup.select('.sister'))
    # （3）通过id查找：
    # pprint(soup.select('#link2'))
    # （4）组合查找：
    # pprint(soup.select('p #link3'))
    # pprint(soup.select('body > a'))
    # （5）通过属性查找：
    # pprint(soup.select('a#link2'))
    # pprint(soup.select('a[href = "http://example.com/tillie"]'))
    # （6）获取内容：
    # pprint(soup.select('title')[0].text)
    # bs4.element.Tag


    #https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/index.html#id41
    #选择多个tag 用 逗号分隔
    # rst = soup.select('title , a')
    #通过tag标签逐层查找:
    # rst = soup.select('body a')
    # rst = soup.select('html head title')

    #找到某个tag标签下的直接子标签
    # rst = soup.select('head > title')
    # rst = soup.select('p > a:nth-of-type(3)')
    # rst = soup.select('p>#link1')
    # rst = soup.select('body > a')
    # rst = soup.select('''img ~ a''')
    # rst = soup.select('p>#link1 + a')
    # rst = soup.select('p>#link1 ~ a')

    #同时用多种CSS选择器查询元素
    # rst = soup.select('#link2 , title')

    #通过是否存在某个属性来查找
    # rst = soup.select('[src]')

    #通过属性的值来查找
    # rst = soup.select('[href="test.org"]')
    # rst = soup.select('[href^="http://example.com"]')
    # rst = soup.select('[href$="lacie"]')
    # rst = soup.select('[href*=".com/el"]')

    #通过语言设置来查找
    # multilingual_markup = """
    #  <p lang="en">Hello</p>
    #  <p lang="en-us">Howdy, y'all</p>
    #  <p lang="en-gb">Pip-pip, old fruit</p>
    #  <p lang="enagb">Pip-pip, old fruit</p>  #en or (en-).*
    #  <p lang="fr">Bonjour mes amis</p>
    # """
    # multilingual_soup = BeautifulSoup(multilingual_markup,'lxml')
    # # en or (en-).*
    # rst = multilingual_soup.select('p[lang|=en]')
    # # [<p lang="en">Hello</p>,
    # #  <p lang="en-us">Howdy, y'all</p>,
    # #  <p lang="en-gb">Pip-pip, old fruit</p>]

    #返回查找到的元素的第一个
    # rst = soup.select_one('[id]')

    #
    # pprint(len(rst))
    # pprint(rst)


    # print(type(soup.prettify()))

    # soup = BeautifulSoup("<a><b /></a>",'lxml')
    # soup = BeautifulSoup("<a><b /></a>",'xml')
    # # soup = BeautifulSoup("<a><b /></a>",'html.parser')
    # soup = BeautifulSoup("<a><b /></a>",'html5lib')
    # print(soup)

    # soup = BeautifulSoup("<a></p>", "lxml")
    # soup = BeautifulSoup("<a></p>", "html5lib")
    # soup = BeautifulSoup("<a></p>", "html.parser")
    #
    # markup = u"<b>\N{SNOWMAN}</b>"
    # snowman_soup = BeautifulSoup(markup)
    # tag = snowman_soup.b
    # print(tag.encode('utf8'))

    #SoupStrainer 解析部分文档
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
        <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    # from bs4 import SoupStrainer
    # only_a_tags = SoupStrainer("a")
    # only_tags_with_id_link2 = SoupStrainer(id="link2")
    # def is_short_string(string):
    #     return len(string) < 10
    # only_short_strings = SoupStrainer(string=is_short_string)

    # print(BeautifulSoup(html, "html.parser", parse_only=only_a_tags).prettify())
    # print(BeautifulSoup(html, "html.parser", parse_only=only_tags_with_id_link2).prettify())
    # print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())
    # print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())


    # from bs4.diagnose import diagnose
    # diagnose(html)

    # print([tag.attrs['href'] for tag in soup.select('a')])
    # print(re.findall(r'<a(.*)</a>',soup.decode('utf-8'),re.S))
    # print(type(soup.decode()))
    pass
