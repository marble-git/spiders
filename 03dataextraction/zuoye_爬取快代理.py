# --coding:utf-8--
"""
@author:marble
@file:zuoye_爬取快代理.py
@date:2021/9/16
"""

import bs4
from bs4 import BeautifulSoup
import time
import requests
import sys
from pprint import pprint


class Content:
    """包含网站中爬取的代理ip的相关属性信息"""

    def __init__(self, ip, port, type: "list", resp_time, anonymity, location, last_verif):
        self.ip = ip
        self.port = port
        self.type = type
        self.resp_time = resp_time
        self.anonymity = anonymity
        self.location = location
        self.last_verif = last_verif

        self.proxy_attrs = [
            self.ip,
            self.port,
            self.type,
            self.resp_time,
            self.anonymity,
            self.location,
            self.last_verif,
        ]

    def __repr__(self):
        return '\n'.join([
            "IP:{}".format(self.ip),
            "PORT:{}".format(self.port),
            "类型:{}".format(self.type),
            "响应时间:{}".format(self.resp_time),
            "匿名度:{}".format(self.anonymity),
            "位置:{}".format(self.location),
            "最后验证时间:{}".format(self.last_verif), ])

    def print(self, file=sys.stdout):
        print(str(self), file=file)

    def tocsvformatstring(self):
        return ','.join(self.proxy_attrs)

    def write2csvfile(self, file=sys.stdout):
        file.write(self.tocsvformatstring() + '\n')


class Website:
    """描述要爬取的网站的结构的信息"""

    def __init__(self, name, base_url, urls: "tuple", tags, attr_tags: "list"):
        self.name = name
        self.base_url = base_url
        self.urls = urls
        self.tags = tags
        self.attr_tags = attr_tags


class Crawler:
    """根据给出的网站信息<site>爬取网站并抓取代理ip信息"""

    def __init__(self, site: "Website", headers, file=sys.stdout, sleep=3):
        """确定要爬取的网站 site
        和结果要保存的文件 file"""
        self.site = site
        self.file = file
        self.headers = headers
        self.sleep = sleep

    @staticmethod
    def get_page(url, headers, sleep=2):
        """请求给定的url,
       如果请求失败返回<None>
       或者<BeautifulSoup 对象>"""
        try:
            resp = requests.get(url=url, headers=headers)
            if sleep is not None:
                # print('sleeping')
                time.sleep(sleep)
                # print('awake', url)
        except requests.exceptions.RequestException as e:
            print(e)
            print(f'<in get_page> request url <{url}> failed')
            return None
        return BeautifulSoup(markup=resp.content.decode('utf-8'), features='lxml')

    def safe_get_text(self, page_obj: "BeautifulSoup", selector):
        """在给定的页面<page_obg>中,根据给定的选择器<selector>搜索文档节点
        并返回该节点中的文本信息
        或者空字符串"""
        selected_tags = page_obj.select(selector)
        if (selected_tags is not None) and (len(selected_tags) > 0):
            return ''.join([tag.get_text(strip=True) for tag in selected_tags])
        return ''

    def parse_page(self, url):
        """根据site解析url指向的页面
        返回Content对象组成的list"""
        # print("in parse_page", url)
        soup = self.get_page(url, headers=self.headers, sleep=self.sleep)
        # print("soup",soup)
        content_list = []
        if soup is not None:
            tag_list = soup.select(self.site.tags)
            # print('tag list',tag_list)
            for tag in tag_list:
                content = self.parse_tag(tag)
                # content.print(file=self.file)
                content.write2csvfile()
                content_list.append(content)
        else:
            print('<in parse_page> something wrong in url <{}> ,skipped'.format(url))

        return content_list

    def parse_tag(self, tag: "bs4.element.Tag"):
        """从包含一项代理ip的tag中
        提取代理IP的相关信息
        并返回Content对象"""
        # print("in parse_tag", tag)
        attrs = []
        for attr_selector in self.site.attr_tags:
            attr = self.safe_get_text(tag, attr_selector)
            attrs.append(attr)
        return Content(*attrs)

    def crawl(self):
        # print("in crawl")
        urls = (self.site.base_url.format(i) for i in range(*self.site.urls))
        for url in urls:
            content_list = self.parse_page(url)
            print('-'*80)
        # print(content_list)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400",
}

if __name__ == '__main__':
    kuaidaili = Website(name="快代理",
                        base_url="https://www.kuaidaili.com/free/inha/{}/",
                        urls=(1, 11, 1),
                        tags="""tbody tr""",
                        attr_tags=[
                            """td[data-title="IP"]""",
                            """td[data-title="PORT"]""",
                            """td[data-title="类型"]""",
                            """td[data-title="响应速度"]""",
                            """td[data-title="匿名度"]""",
                            """td[data-title="位置"]""",
                            """tr td[data-title="最后验证时间"]""",
                        ])
    wandou = Website(name="豌豆HTTP",
                     base_url="https://h.wandouip.com/?page={}#sec3",
                     urls=(1,11,1),
                     tags="""table tr ~ tr""",
                     attr_tags=[
                         """td:nth-child(1)""",
                         "aa",
                         """td:nth-child(3)""",
                         "aa",
                         """td:nth-child(2)""",
                         """td:nth-child(4)""",
                         """td:nth-child(5)""",
                     ])

    sites = [
        # kuaidaili,
        wandou
    ]
    for site in sites:
        crawler = Crawler(site, headers=headers, sleep=5, file=sys.stdout)
        crawler.crawl()
