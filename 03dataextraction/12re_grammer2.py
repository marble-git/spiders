# --coding:utf-8--
"""
@author:marble
@file:12re_grammer2.py
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
    # * : 对它前面的正则式匹配0到任意次重复， 尽量多的匹配字符串。
    # text = '+abc13'
    # pattern =  r'\w*'

    # + : 对它前面的正则式匹配1到任意次重复。
    # text = 'abc'
    # pattern = r'\w+?'

    # ? : 对它前面的正则式匹配0到1次重复。
    # text = '12abc'
    # pattern = r'\w?'

    # {m} : 对其之前的正则式指定匹配 m 个重复；少于 m 的话就会导致匹配失败
    # text = '987f12abc'
    # pattern = r'(\d{2})?'

    # {m,n} : 对正则式进行 m 到 n 次匹配，在 m 和 n 之间取尽量多
    text = '98-7f12abc'
    pattern = r'\w{1,3}'

    # 输出结果
    rmch = re.match(pattern, text)
    rst = rmch.group()
    print(rst)
    logger.info(repr(rst))
