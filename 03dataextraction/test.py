# --coding:utf-8--
"""
@author:marble
@file:test.py
@date:2021/9/5
"""

import bs4
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time
import re


def get_tag_text(soup: "BeautifulSoup", selector: "css_selector or re.Pattern"):
    if isinstance(selector, str):
        tags = soup.select(selector)
        return ''.join([tag.get_text(strip=True) for tag in tags])

    elif isinstance(selector, re.Pattern):
        html = re.findall(selector, soup.decode('utf-8'))[0]
        tag = BeautifulSoup(html, 'lxml')
        return tag.get_text(strip=True).rsplit(':',1)[-1]


if __name__ == '__main__':
    url = "https://movie.douban.com/subject/1418019/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400"
    }
    resp = requests.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    selectors = [
        "h1 > span",
        "a[rel='v:directedBy']",
        "span.pl:-soup-contains('编剧') + span",
        "span.pl:-soup-contains('主演') ~ span",
        re.compile(r"""<span class="pl">\s*类型.*?</span>\s*<br/>""", re.S),
        re.compile(r"""<span class="pl">\s*制片国家.*?<br/>""", re.S),
        re.compile(r"""<span class="pl">\s*语言.*?<br/>""", re.S),
        re.compile(r"""<span class="pl">\s*上映日期.*?</span>\s*<br/>""", re.S),
        "span[property='v:runtime']",
        re.compile(r"""<span class="pl">\s*又名.*?<br/>""", re.S),
        re.compile(r"""<span class="pl">\s*IMDb.*?<br/>""", re.S),
        "strong",
    ]
    for selector in selectors:
        text = get_tag_text(soup, selector)
        print(text)
        print('-' * 60)
    bs4.element.Tag
    pass
