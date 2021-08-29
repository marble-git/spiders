# --coding:utf-8--
"""
@author:marble
@file:07find和find_all.py
@date:2021/8/29
"""

import bs4
from bs4 import BeautifulSoup
from pprint import pprint

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""
# 0. 获取第一个tr标签
# 1. 获取所有tr标签
# 2. 获取第2个tr标签
# 3. 获取所有class等于even的tr标签
# 4. 将所有id等于test，class也等于test的a标签提取出来。
# 5. 获取所有a标签的href属性
# 6. 获取所有的职位信息（纯文本）
if __name__ == '__main__':
    soup = BeautifulSoup(html,'lxml')
    # 0. 获取第一个tr标签
    # tr1 = soup.tr
    # print(tr1)
    # tr1_ = soup.find('tr')
    # print(tr1 is tr1_) # True
    # print(tr1_)
    # 1. 获取所有tr标签
    # trs = soup.find_all('tr')
    # pprint(trs,indent=4)
    # for tr in trs:
    #     print('-'*80)
    #     print(tr)
    # 2. 获取第2个tr标签
    # tr2 = soup.find_all('tr')[1]
    # tr2_1 = soup.find('tr',attrs={'class':'even'})
    # tr2_2 = soup.find_all('tr',limit=2)[-1]
    # print(tr2 is tr2_1 and tr2 is tr2_2)
    # print(tr2)
    # 3. 获取所有class等于even的tr标签
    # evens = soup.find_all('tr',attrs={'class':'even'})
    # evens_1 = soup.find_all('tr',class_ = 'even')
    # print(evens == evens_1)  # ==, not is
    # print(evens_1)
    # for even in evens:
    #     print('-'*80)
    #     print(even)
    # 4. 将所有id等于test，class也等于test的a标签提取出来。
    # all_a = soup.find_all('a',attrs={'id':'test','class':'test'})
    # all_a_1 = soup.find_all('a',id='test',class_='test')
    # print(all_a == all_a_1) #eq ,not is
    # print(all_a)
    # 5. 获取所有a标签的href属性
    # aa = soup.find_all('a')
    # hrefs = [a['href'] for a in aa]
    # hrefs_1 = [a.attrs.get('href') for a in aa]  #a.attrs 是 个 字典 dict
    # print(hrefs == hrefs_1) #eq ,not is
    # pprint(hrefs_1)
    # 6. 获取所有的职位信息（纯文本）
    # trs = soup.find_all('tr')[1:]
    # infos = [list(tr.stripped_strings) for tr in trs] #strings,stripped_strings 都返回生成器(generator)
    # pprint(infos)
    soup.select()
    pass
