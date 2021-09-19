# re 正则表达式

## 单字符匹配


+ `re.match(pattern, string, flags=0)`: 该方法中的参数 `pattern`默认从`string`的开始进行匹配
+ 即 `re.search(pattern = '^' + pattern,string,flags=0)`

```python

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

    # $
    text = 'foo1\nfoo2\nfoo'
    pattern = r'foo$'

    # 输出结果
    rmch = re.match(pattern, text)
    rst = rmch.group()
    print(rst)
    logger.info(repr(rst))
```


## 多字符匹配

```python
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

```


## 正则表达式案例

```python
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

```


## 开始(`^`)/结束(`$`)/贪婪(`*,+,?`)和非贪婪(`*?,+?,??`)

+ re.M 
+ re.MULTILINE 
+ 设置以后，样式字符 '^' 匹配字符串的开始，和每一行的开始（换行符后面紧跟的符号）；
+ 样式字符 '$' 匹配字符串尾，和每一行的结尾（换行符前面那个符号）。默认情况下，’^’ 匹配字符串头，'$' 匹配字符串尾。对应内联标记 (?m) 
    

```python
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

    # ^：以...开头：(插入符号) 匹配字符串的开头， 并且在 MULTILINE 模式也匹配换行后的首个符号。
    # text = "hello world\n123"
    # pattern = r'^\w+'
    # pattern = r'^'

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


    # 案例2：验证一个字符是不是0-100之间的数字：
    # 0,1,99,100
    # 01
    text = "0,1 12 99 100 101 02 11b 9u 1000"
    # pattern = r'\b(0|100|[1-9]\d?)\b'
    pattern = r'\b(0|[1-9]\d?|100)\b'


    # 输出结果
    # rmch = re.findall(pattern, text,re.M)
    rmch = re.findall(pattern, text)
    # rst = rmch.group()
    rst = rmch
    print(rst)
    logger.info(repr(rst))
```


