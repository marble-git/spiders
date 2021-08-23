# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/21
"""

import lxml
from lxml import etree

html = etree.parse('hello.html')
print(html)
if __name__ == "__main__":
    # 在lxml中使用XPath语法:
    # 1.获取所有li标签:
    result = html.xpath('//li')
    for i in result:
        print(etree.tostring(i))
    # 2.获取所有li元素下的所有class属性的值:
    result = html.xpath('//li/@class')
    # 3.获取li标签下href为www.baidu.com的a标签:
    result = html.xpath('''//li//a[@href='www.baidu.com']''')
    # 4.取li标签下所有span标签:
    result = html.xpath('//li//span')
    # 5.获取li标签下的a标签里的所有class:
    result = html.xpath('//li//a//@class')
    # 6.获取最后一个li的a的href属性对应的值:
    result = html.xpath('//li[last()]/a/@href')
    # 7.获取倒数第二个li元素的内容:
    result = html.xpath('//li[last()-1]//text()')
    # 8.获取倒数第二个li元素的内容的第二种方式:
    result = html.xpath('//li[last()-1]/a')
    print(result[0].text)

    
    print(result,'klk')
    print(result[0].xpath('./attribute::*'))
    # print(result[0].tag)
    # print(result[0].tail)
    # print(result[0].text)
    # print(result[0].values())
    # print(result[0].xpath)
    pass
