# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/9
"""

import os
from urllib import request

request.urlretrieve('http://5b0988e595225.cdn.sohucs.com/images/20180528/209f099433dd459ba9a56658f5911c27.jpeg',
                    "02request/sylm.jpeg")

print(os.listdir())




