# --coding-utf-8--

"""
@file:biquge.py
@author:marble
@date:2021/8/24
"""

import lxml
import time
import requests
from lxml import etree
from collections import namedtuple

NovelMeta = namedtuple('NovelMeta', 'name author intro')
NovelState = namedtuple('NovelState', 'lastupdate lastchapter')
NovelChapter = namedtuple('Chapter', 'title chapter_url')


class Novel:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    def __init__(self, start_url):
        self.start_url = start_url

    def parse_page(self):
        response = requests.get(self.start_url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        self.getnovelinfo(html)
        self.getnovelchapters(html)

    def getnovelchapters(self, html):
        self.chapters = []
        chapter_node_list = html.xpath("//div[@id='list']//a")
        for chapter_node in chapter_node_list:
            title = chapter_node.xpath('.//text()')[0]
            url = self.start_url + chapter_node.xpath('./@href')[0]
            chapter = NovelChapter(title, url)
            self.chapters.append(chapter)

    def getnovelinfo(self, html):
        novel_name = html.xpath('//h1//text()')[0]
        novel_author = html.xpath("//div[@id='info']/p[1]//text()")[0].split('：')[1]
        novel_introducton = html.xpath("//div[@id='intro']/p[1]//text()")[0].strip()
        last_updated_chapter = html.xpath("//div[@id='info']/p[4]//text()")[1]
        last_updated_time = html.xpath("//div[@id='info']/p[3]//text()")[0].split('：')[1]
        self.novelmeta = NovelMeta(novel_name, novel_author, novel_introducton)
        self.novelstate = NovelState(last_updated_time, last_updated_chapter)

    def parse_detail(self,detail_url):
        pass

    def action(self):
        self.parse_page()

    def pre_check(self):
        pass


if __name__ == "__main__":
    novel = Novel('https://www.ibswtan.com/54/54307/')
    novel.action()
