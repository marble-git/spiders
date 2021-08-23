# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/20
"""

import lxml
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>                                             
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''


if __name__ == "__main__":
    html = etree.HTML(text)
    html = etree.parse('hello.html')
    print(html)
    # print(etree.tostring(html,pretty_print=True).decode('utf-8'))
    # print(etree.tostring(html))
    print(etree.tostring(html,method='text'))
    pass
