# --coding-utf-8--

"""
@file:03practice_xiaohua.py
@author:marble
@date:2021/8/23
"""

import lxml
import time
import requests
import json
from lxml import etree


def geturl(page):
    return f"https://xiaohua.zol.com.cn/new/{page}.html"


def parse_page(page_url, *, headers):
    domain = "https://xiaohua.zol.com.cn"
    response = requests.get(page_url, headers=headers)
    text = response.text
    # print(text)
    html = etree.HTML(text)
    # print(html)
    detail_url_list = html.xpath("//div/a[@class='all-read']/@href")
    detail_url_list = [domain + detail_url for detail_url in detail_url_list[:]]
    return detail_url_list


def parse_detail(detail_url, *, headers):
    response = requests.get(detail_url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    joke_title = html.xpath('//h1/text()')
    joke_content = html.xpath("//div[@class='article-text']//text()")
    joke_title = ''.join(joke_title)
    joke_content = ''.join(joke_content)
    joke = {joke_title: joke_content}
    # print(joke_title)
    # print(joke_content)
    # print(joke)
    # print(f'<{joke_title}> downloaded.')
    return joke


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}


def main():
    joke_list = []
    for page in range(1, 11):
        page_url = geturl(page)
        detail_url_list = parse_page(page_url, headers=headers)
        for detail_url in detail_url_list:
            joke = parse_detail(detail_url, headers=headers)
            joke_list.append(joke)
            print(f"page:{page},<{tuple(joke.keys())[0]}> downloaded")
            time.sleep(2)
        print(f"page {page} done.")
        print('-' * 80)
        time.sleep(2)
    print('=' * 80)
    print('all downloaded')
    return joke_list


if __name__ == "__main__":
    joke_list = main()
    with open('jokes.json', 'w', encoding='utf-8') as f:
        json.dump(joke_list, f, ensure_ascii=False)
