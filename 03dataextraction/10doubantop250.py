# --coding:utf-8--
"""
@author:marble
@file:10doubantop250.py
@date:2021/9/4
"""

import bs4
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time
import re
import sys
import tqdm
from tqdm import tqdm


class Content:
    """包含每一部电影要抓取的信息"""

    def __init__(self,
                 film,
                 director,
                 screenwriter,
                 starring,
                 type,
                 production_country,
                 language,
                 release_date,
                 film_length,
                 also_known_as,
                 IMDB,
                 stars):
        """每一部电影要抓取的信息的属性"""
        self.film = film
        self.director = director
        self.screenwriter = screenwriter
        self.starring = starring
        self.type = type
        self.production_country = production_country
        self.language = language
        self.release_date = release_date
        self.film_length = film_length
        self.also_known_as = also_known_as
        self.IMDB = IMDB
        self.stars = stars

        self.film_attrs = [self.film,
                           self.director,
                           self.screenwriter,
                           self.starring,
                           self.type,
                           self.production_country,
                           self.language,
                           self.release_date,
                           self.film_length,
                           self.also_known_as,
                           self.IMDB,
                           self.stars, ]

    def print(self, *, file=sys.stdout, left=10):
        """以灵活的方式输出该电影实例的相关抓取信息"""
        print('{0:>{2:}} : {1:}'.format('电影名', self.film, left),
              '{0:>{2:}} : {1:}'.format('导演', self.director, left),
              '{0:>{2:}} : {1:}'.format('编剧', self.screenwriter, left),
              '{0:>{2:}} : {1:}'.format('主演', self.starring, left),
              '{0:>{2:}} : {1:}'.format('类型', self.type, left),
              '{0:>{2:}} : {1:}'.format('制片国家/地区', self.production_country, left),
              '{0:>{2:}} : {1:}'.format('语言', self.language, left),
              '{0:>{2:}} : {1:}'.format('上映日期', self.release_date, left),
              '{0:>{2:}} : {1:}'.format('片长', self.film_length, left),
              '{0:>{2:}} : {1:}'.format('又名', self.also_known_as, left),
              '{0:>{2:}} : {1:}'.format('IMDb', self.IMDB, left),
              '{0:>{2:}} : {1:} 星'.format('豆瓣评分', self.stars, left),
              sep='\n', file=file)

    def tocsvformatstring(self):
        return ','.join(self.film_attrs)

    def write2csvfile(self, file=sys.stdout):
        string = self.tocsvformatstring()
        return file.write(string + '\n')


class Website:
    """描述网站结构的信息"""

    def __init__(self,
                 name,
                 urls,
                 detail_url_tag: "css selector",
                 absolute_url,
                 detail_attrs_tags: "css selectors or re.Pattern"
                 ):
        self.name = name
        self.urls = urls
        self.detail_url_tag = detail_url_tag
        self.absolute_url = absolute_url
        self.detail_attrs_tags = detail_attrs_tags


class Crawler:
    """抓取目标网站<site>中的电影详情信息"""

    def __init__(self, site: "Website", headers):
        """由网站结构信息<Website obj>
        和请求头信息<headers>实例化一个爬虫对象"""
        self.site = site
        self.headers = headers

    def get_page(self, url, headers, sleep=None):
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

    def safe_get_tag_text(self, page_obj: "BeautifulSoup", selector: "css str or re.Pattern"):
        """在给定的页面<page_obg>中,根据给定的选择器<selector>搜索文档节点
        并返回该节点中的文本信息
        或者空字符串"""
        if isinstance(selector, str):
            selected_tags = page_obj.select(selector)
            if (selected_tags is not None) and (len(selected_tags) > 0):
                return ''.join([tag.get_text(strip=True) for tag in selected_tags])
            return ''
        if isinstance(selector, re.Pattern):
            rst_list = re.findall(selector, page_obj.decode('utf-8'))
            if len(rst_list) > 0:
                html = rst_list[0]
                tag = BeautifulSoup(html, 'lxml')
                return tag.get_text(strip=True).rsplit(':', 1)[-1]
            return ''

    def parse_main(self, urls, sleep=None):
        """解析概览页面,返回包含电影详情页面的url的<list 列表>"""
        detail_urls = []
        for url in tqdm(urls,desc='处理概览页面',unit='页',unit_scale=True):
            # soup = self.get_page(url, self.headers, sleep=0.5)
            soup = self.get_page(url, self.headers, sleep)
            # print(soup.decode('utf-8'))
            if soup is not None:
                detail_url_tags = soup.select(self.site.detail_url_tag)
                for detail_url_tag in detail_url_tags:
                    detail_url = detail_url_tag['href']
                    detail_urls.append(detail_url)
                    # print(detail_url)
            else:
                print('<in parse_main> something wrong in url <{}> ,skipped'.format(detail_url))
        return detail_urls

    def parse_detail(self, url, sleep=None):
        """解析电影详情页面，返回包含电影详情信息的<Content 对象>"""
        # soup = self.get_page(url, self.headers, sleep=1)
        soup = self.get_page(url, self.headers, sleep)
        # print(url)
        detail_attrs = []
        if soup is not None:
            for detail_attr_selector in self.site.detail_attrs_tags:
                detail_attr = self.safe_get_tag_text(soup, detail_attr_selector)
                detail_attrs.append(detail_attr)
            # print(detail_attrs)
            return Content(*detail_attrs)
        print('<in parse_detail> something wrong in url <{}> ,skipped'.format(detail_url))
        return None

    def crawl(self, *, start,file=sys.stdout, sleep=1):
        """抓取所有电影详情
        返回所有电影详情<Content obj>的列表<list>"""
        detail_urls = self.parse_main(self.site.urls, sleep)
        # detail_urls = ['https://movie.douban.com/subject/26393561/']
        # pprint(detail_urls)
        # print(len(detail_urls))
        # print('-' * 60)
        contents = []
        for detail_url in tqdm(detail_urls[start:],desc='处理详情页',unit='页',unit_scale=True):
        # for detail_url in detail_urls:
            content = self.parse_detail(detail_url, sleep)
            if content is None:
                print('<in crawl> something wrong in url <{}> ,skipped'.format(detail_url))
                continue
            # content.print(file=file)
            content.write2csvfile(file=file)
            # contents.append(content)
        # return contents
        # break


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400",
    "Cookie": """ll="118096"; bid=Gpfd_XeoKwI; __yadk_uid=DE0uawMZq5coB0KTXkfKYwmFaLW3rlgV; __gads=ID=c0824b4c7ba3c76d-221c3c058acb00f3:T=1630759436:RT=1630759436:S=ALNI_Mbmgzk3powfZlLGgvRaQ8E22hjZhQ; __utmc=30149280; dbcl2="221442636:OYoKmUbwqS4"; ck=97AR; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1631025449%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fwww.douban.com%252Fnote%252F809408645%252F%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.1599395192.1630759402.1631020224.1631025452.6; __utmz=30149280.1631025452.6.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt=1; __utmv=30149280.22144; _pk_id.100001.8cb4=7cdd747fbb0f1400.1630759400.2.1631025454.1630759436.; __utmb=30149280.4.10.1631025452"""
}
if __name__ == '__main__':
    douban_base_url = 'https://movie.douban.com/top250?start={}&filter='
    doubanTop250 = Website(name='豆瓣 Top250',
                           urls=(douban_base_url.format(start) for start in range(0, 250, 25)),
                           detail_url_tag='div.hd > a',
                           absolute_url=True,
                           detail_attrs_tags=[
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
                           ])

    crawler = Crawler(doubanTop250, headers=headers)
    # contents = crawler.crawl()
    with open('top250.csv', 'at', encoding='utf-8') as f:
        crawler.crawl(start=192,file=f,sleep=5)

    # args = ['肖申克的救赎 The Shawshank Redemption(1994)', '弗兰克·德拉邦特', '弗兰克·德拉邦特/斯蒂芬·金', '蒂姆·罗宾斯/摩根·弗里曼/鲍勃·冈顿/威廉姆·赛德勒/克兰西·布朗/吉尔·贝罗斯/马克·罗斯顿/詹姆斯·惠特摩/杰弗里·德曼/拉里·布兰登伯格/尼尔·吉恩托利/布赖恩·利比/大卫·普罗瓦尔/约瑟夫·劳格诺/祖德·塞克利拉/保罗·麦克兰尼/芮妮·布莱恩/阿方索·弗里曼/V·J·福斯特/弗兰克·梅德拉诺/马克·迈尔斯/尼尔·萨默斯/耐德·巴拉米/布赖恩·戴拉特/唐·麦克马纳斯', '剧情/犯罪', '美国', '英语', '1994-09-10(多伦多电影节)/1994-10-14(美国)', '142分钟', '月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎', 'tt0111161', '9.7']
    # cnt = Content(*args)
    # print(cnt)
    # cnt.print(3)
    pass
