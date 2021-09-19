# --coding:utf-8--
"""
@author:marble
@file:13re_grammer3.py
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
    #正则表达式案例


    # 1. 验证手机号码：手机号码的规则是以1开头，第二位可以是34587，后面那9位就可以随意了。
    # text = "18677889900"
    # pattern = r'1[34578]\d{9}'

    # 2. 验证邮箱：邮箱的规则是邮箱名称是用数字、英文字符、下划线组成的，然后是@符号，后面就是域名了。
    # text = "hynever@163.com"
    # domain= r'(\w+\.)\w+'
    # pattern = r'\w+@' + domain


    # 3. 验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。
    # text = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    # pattern = r'(http|https|ftp)://\S+'

    # 4. 验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。
    text = "36530019870716234X"
    pattern = r'\d{17}[\dxX]'


    # 输出结果
    rmch = re.match(pattern, text)
    rst = rmch.group()
    print(rst)
    logger.info(repr(rst))
