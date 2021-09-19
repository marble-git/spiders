# --coding:utf-8--
"""
@author:marble
@file:14开始结束非贪婪.py
@date:2021/9/19
"""

import re
import logging
import sys


def init_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(levelname)-6s:%(name)s:%(funcName)-9s:%(message)s")
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger


if __name__ == '__main__':
    logger = init_log()

    #re.M
    #re.MULTILINE
    #设置以后，样式字符 '^' 匹配字符串的开始，和每一行的开始（换行符后面紧跟的符号）；样式字符 '$' 匹配字符串尾，和每一行的结尾（换行符前面那个符号）。默认情况下，’^’ 匹配字符串头，'$' 匹配字符串尾。对应内联标记 (?m)

    # ^：以...开头：(插入符号) 匹配字符串的开头， 并且在 MULTILINE 模式也匹配换行后的首个符号。(re.M)
    # text = "hello world\n123"
    # pattern = r'^\w+'
    pattern = r'^'

    # $：以...结尾：匹配字符串尾或者在字符串尾的换行符的前一个字符，在 MULTILINE 模式下也会匹配换行符之前的文本。
    # text = 'hello world hefgh\n123'
    # pattern = r'\w+$'
    # pattern = r'$'

    # |：匹配多个字符串或者表达式：
    # A|B， A 和 B 可以是任意正则表达式，创建一个正则表达式，匹配 A 或者 B.
    # #任意个正则表达式可以用 '|' 连接。
    # '|' 操作符绝不贪婪。
    # 如果要匹配 '|' 字符，使用 \|， 或者把它包含在字符集里，比如 [|].
    # text = 'abc 123 /*- 1abc 123a abc123'
    # pattern = r'\b(abc|123)\b'

    # 贪婪(*,+,?)在字符串进行尽可能多的匹配;和非贪婪(*?,+?,??)：
    # 如果正则式 <.*> 希望找到 '<a> b <c>'，它将会匹配整个字符串，而不仅是 '<a>'。
    # 在修饰符之后添加 ? 将使样式以 非贪婪 方式匹配: 使用正则式 <.*?> 将会仅仅匹配 '<a>'。
    # text = "'<a> b <c>"
    # pattern = r'<.*>'
    # pattern = r'<.*?>'

    # 案例1：提取html标签名称：
    # text = "<h1>这是标题</h1>"
    # pattern = r'<.+?>(.*)<.+?>'
    # pattern = '<.+?>'


    # 案例2：验证一个字符是不是0-100之间的数字：
    # 0,1,99,100
    # 01
    # text = "0,1 12 99 100 101 02 11b 9u 1000"
    # # pattern = r'\b(0|100|[1-9]\d?)\b'
    # pattern = r'\b(0|[1-9]\d?|100)\b'


    # 输出结果
    # rmch = re.findall(pattern, text,re.M)
    rmch = re.findall(pattern, text)
    # rst = rmch.group()
    rst = rmch
    print(rst)
    logger.info(repr(rst))
