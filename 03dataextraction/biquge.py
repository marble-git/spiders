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
NovelChapter = namedtuple('NovelChapter', 'id title chapter_url')
ChapterContent = namedtuple('ChapterContent', 'title content')


def writenamedtuple(ntuple):
    return '\n'.join(ntuple)


class Novel:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }

    def __init__(self, start_url, savedir=os.curdir):
        self.start_url = start_url
        self.savedir = savedir

    def parse_page(self):
        """解析小说首页
                获取小说的
                元信息：小说名字，作者，简介
                最新状态：最后更新时间，最后更新状态
                小说章节：章节名，可以获取的URL
        """
        response = requests.get(self.start_url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        self.getnovelinfo(html)
        self.getnovelchapters(html)

    def getnovelchapters(self, html):
        """解析小说首页
                获取小说的
                小说章节：章节名，可以获取的URL
                """
        self.chapters = []
        chapter_node_list = html.xpath("//div[@id='list']//a")
        for id, chapter_node in zip(range(1, len(chapter_node_list) + 1), chapter_node_list):
            title = chapter_node.xpath('.//text()')[0]
            url = self.start_url + chapter_node.xpath('./@href')[0]
            chapter = NovelChapter(str(id).zfill(4), title, url)
            self.chapters.append(chapter)

    def getnovelinfo(self, html):
        """解析小说首页
                获取小说的
                元信息：小说名字，作者，简介
                """
        novel_name = html.xpath('//h1//text()')[0]
        novel_author = html.xpath("//div[@id='info']/p[1]//text()")[0].split('：')[1]
        novel_introducton = html.xpath("//div[@id='intro']/p[1]//text()")[0].strip()
        # last_updated_chapter = html.xpath("//div[@id='info']/p[4]//text()")[1]
        # last_updated_time = html.xpath("//div[@id='info']/p[3]//text()")[0].split('：')[1]
        self.novelmeta = NovelMeta(novel_name, novel_author, novel_introducton)

    def parse_detail(self, detail_url):
        """解析小说的每一章
        返回每一章的详细信息：章节名，本章正文"""
        response = requests.get(detail_url, headers=self.headers)
        text = response.content.decode('utf-8')
        html = etree.HTML(text)
        title = html.xpath('//h1/text()')[0]
        # print(title)
        chapter_content = html.xpath("//div[@id='content']/text()")
        chapter_content = [string.strip('\xa0') for string in chapter_content[:]]
        chapter_content = '\n'.join(chapter_content)
        return ChapterContent(title, chapter_content)

    def is_updated(self):
        """判断到目前为止该小说是否更新了
        并初始化小说的保存目录和相关元信息"""
        savepath = os.path.join(self.savedir, self.novelmeta.name)
        self.savepath = savepath
        if not os.path.isdir(savepath):
            os.mkdir(savepath)
            print('directory <{}> created.'.format(savepath))
        if not os.path.exists(path := os.path.join(savepath, 'novelmeta.txt')):
            with open(path, 'wt', encoding='utf-8', newline='') as f:
                f.write(writenamedtuple(self.novelmeta))
                print(f'<{path}> created.')
        if not os.path.exists(path := os.path.join(savepath, 'downloaded.txt')):
            with open(path, 'wt', encoding='utf-8', newline='') as f:
                print(f'<{path}> created.')
        if not os.path.exists(path := os.path.join(savepath, 'newupdate.txt')):
            with open(path, 'wt', encoding='utf-8', newline='') as f:
                print(f'<{path}> created.')

        with open(os.path.join(self.savepath, 'downloaded.txt'), 'rt', encoding='utf-8') as f:
            downloaded_text = f.readlines()
        existed_chapters = [eval(record.strip('\n')) for record in downloaded_text]
        self.newupdate = []

        for chapter in self.chapters:
            if chapter in existed_chapters:
                # print(chapter, 'existed')
                continue
            print(chapter, 'new updated')
            self.newupdate.append(chapter)
        if not self.newupdate:
            print('not updated')
            return False
        else:
            print('updated')
            return True

    def update(self):
        """获取最新更新的章节
        下载新更新的章节"""
        with open(os.path.join(self.savepath, 'newupdate.txt'), mode='at', encoding='utf-8') as f:
            f.write('-' * 80 + '\n')
        for chapter in self.newupdate:
            time.sleep(10)
            newcontent = self.parse_detail(chapter.chapter_url)
            print(chapter, 'downloaded.')
            self.save_chapter(chapter, newcontent)

    def save_chapter(self, chapter, newcontent):
        """保存章节内容
        并更新记录文件
        downloaded.txt
        newupdate.txt"""
        with open(os.path.join(self.savepath, chapter.id + newcontent.title + '.txt'), mode='wt',
                  encoding='utf-8') as f:
            f.write(newcontent.content + '\n')

        if chapter.id + chapter.title + '.txt' in os.listdir(self.savepath):
            with open(os.path.join(self.savepath, 'downloaded.txt'), mode='at', encoding='utf-8') as f:
                f.write(repr(chapter) + '\n')
            with open(os.path.join(self.savepath, 'newupdate.txt'), mode='at', encoding='utf-8') as f:
                f.write(repr(chapter) + '\n')
            print(newcontent.title, 'saved.')
        else:
            print(newcontent.title, 'save failed.')

    def activate(self):
        self.parse_page()
        if self.is_updated():
            self.update()
        print('all updated.')
        return True


if __name__ == "__main__":
    mingzun_url = 'https://www.ibswtan.com/54/54307/'
    save_to = r'C:\Users\MARBLE\Desktop\novels'
    novel = Novel(mingzun_url, save_to)
    while True:
        try:
            novel.activate()
            time.sleep(600)
        except KeyboardInterrupt:
            print(KeyboardInterrupt, 'EXIT')
            exit()
        except:
            pass
