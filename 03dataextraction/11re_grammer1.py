# --coding:utf-8--
"""
@author:marble
@file:11re_grammer1.py
@date:2021/9/18
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
    # #匹配某个字符 CHAR
    # text = 'abc'
    # # pattern = 'a'
    # pattern = 'b'
    # rst = re.match(pattern,text)
    # print(rst.group(),type(rst.group()))
    # logger.info(rst.group())

    # # (.) 匹配任意单个字符 (除了 '\n')
    # text = '\rabc'
    # pattern = '.'
    # rst = re.match(pattern, text)
    # print(repr(rst.group()), type(rst.group()))
    # # logger.info(rst.group())

    # # \d : 匹配任意的单个数字([0-9])
    # text = '-abc'
    # pattern = '\d'

    # # \D : 匹配任意的单个 非数字([^0-9])
    # text = '\nabc'
    # text = '\rabc'
    # text = '9abc'
    # pattern = '\D'

    # # \s : 匹配任意的单个空白字符([\f\v\n\t\r ])
    # text = '\v\f \r\t\n-abc'
    # pattern = '\s'
    # # pattern = '[\f\v\n\t\r ]'

    # # \S : 匹配任意的单个非空白字符([^\f\v\n\t\r ])
    # text = '?.\v\f \r\t\n-abc'
    # pattern = '\S'

    # # \w : 匹配任意的单个变量构成要素([_a-zA-Z0-9])
    # text = 'abcSDF9035_79\n/*-'
    # pattern = '\w*'


    # \W : 匹配任意的非单个变量构成要素([^_a-zA-Z0-9])
    # text = '*-\n \r()}]^abcSDF9035_79\n/*-'
    # pattern = '\W*'


    # []组合的方式 : 只要满足 中括号 里面的某一项就匹配成功
    # text = 'ghsDS-1 2*-02345\n \r()}]^abcSDF9035_79\n/*-'
    # pattern = '[1\-23s *]*'
    # pattern = '[A-z]*'


    # # \A 只匹配字符串开始  (^)
    # text = 'abcd124'
    # pattern = '.*\A.'

    # # 输出结果
    # rmch = re.match(pattern, text)
    # rst = rmch.group()
    # print(rst)
    # logger.info(repr(rst))

    #\b 匹配空字符串: \w 和 \W 字符的[空字符串边界]，或者 \w 和字符串开始/结尾的边界
    # r = re.split(r'\b123\b','==123!! abc123,123,123==abc,123')
    # logger.debug(r)
    # text = '==123!! abc123,123==p,123,123a\nbc,123'
    # pattern = r'\b123=\b'

    #\B 匹配空字符串: 但 不 能在词的开头或者结尾
    #\w与\w的[空字符边界];#\W与\W的[空字符边界];
    # text = '==123!! abc123,123,123a\nbc,123'
    # pattern = r'\B123'

    # text = '1_py=cthon py5 2py=342 py==1py2py4 pyp3 3py= pyabc'
    # pattern = r'py=\B'
    # pattern = r'\Bpy'
    # text = '*abc/*-='
    # pattern = r'\B'
    # pattern = r'\b'
    # 输出结果
    # rmch = re.split(pattern, text)
    # rst = rmch
    # print(rst)
    # logger.info(repr(rst))

    # $ : 匹配字符串尾或者在字符串尾的换行符的前一个字符
    text = 'foo1\nfoo2\n'
    pattern = r'foo.$'
    pattern = r'$'

    # 输出结果
    rmch = re.search(pattern, text)
    rst = rmch.group()
    print(rst)
    logger.info(repr(rst))



