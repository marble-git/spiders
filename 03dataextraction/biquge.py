# --coding-utf-8--

"""
@file:biquge.py
@author:marble
@date:2021/8/24
"""

import lxml
import time
import os
import requests
from lxml import etree
from collections import namedtuple

NovelMeta = namedtuple('NovelMeta', 'name author intro')
NovelState = namedtuple('NovelState', 'lastupdate lastchapter')
NovelChapter = namedtuple('Chapter', 'title chapter_url')
ChapterContent = namedtuple('ChapterContent', 'title content')


def writenamedtuple(ntuple):
    return '\n'.join(ntuple)


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

    def parse_detail(self, detail_url):
        response = requests.get(detail_url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        title = html.xpath('//h1/text()')[0]
        print(title)
        chapter_content = html.xpath("//div[@id='content']/text()")
        chapter_content = [string.strip('\xa0') for string in chapter_content[:]]
        chapter_content = '\n'.join(chapter_content)
        return ChapterContent(title, chapter_content)

    def action(self):
        self.parse_page()
        self.updated()
        for chapter in self.chapters:
            c = self.parse_detail(chapter.chapter_url)
            # print(chapter.title)
            # print(c.title == chapter.title)
            # print(c)
            break

    def updated(self):
        if not os.path.isdir(self.novelmeta.name):
            os.mkdir(self.novelmeta.name)
            print('directory <{}> created.'.format(self.novelmeta.name))
        if not os.path.exists(path := os.path.join(self.novelmeta.name, 'novelmeta.txt')):
            with open(path, 'wt', encoding='utf-8') as f:
                f.write(writenamedtuple(self.novelmeta))
                print(f'<{path}> created.')
        if not os.path.exists(path := os.path.join(self.novelmeta.name, 'novelstate.txt')):
            with open(path, 'wt', encoding='utf-8') as f:
                f.write(writenamedtuple(self.novelstate))
                print(f'<{path}> created.')

        with open(os.path.join(self.novelmeta.name,'novelstate.txt')) as f:
            text = f.readlines()
        text = [line.strip('\n') for line in text]
        laststate = NovelState(text[0],text[1])
        print(laststate)
        if self.novelstate == laststate:
            print('not updated')
            # return False
        self.existing_chapters = os.listdir(self.novelmeta.name)
        # self.existing_chapters = [chapter if ]
        print(self.existing_chapters)
        print('updated')
        return True


if __name__ == "__main__":
    novel = Novel('https://www.ibswtan.com/54/54307/')
    novel.action()
