# BeautifulSoup基本使用

## BeautifulSoup4库

+ 和lxml一样，`BeautifulSoup`也是一个HTML/XML的解析器，主要功能也是解析和提取HTML/XML数据
+ `lxml` 只会局部遍历，而 `BeautifulSoup` 是基于HTML DOM(Document Object Model)的，会载入整个DOM树，因此时间和内存开销都会大很多，所以性能要低于`lxml`
+ `Beautiful Soup 3` 目前已经停止开发，推荐现在的项目使用 `BeautifulSoup4`

## 安装和文档

+ 安装：`pip install bs4`
+ 中文文档：`https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html`

## 几大解析工具对比

解析工具 | 解析速度 |使用难度
-------|---------|-------
BeautifulSoup|最慢|最简单
lxml|快|简单
re|最快|最难

## 简单使用：


```python
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

if __name__ == '__main__':
    # soup = BeautifulSoup(html)
    # print(soup)
    soup = BeautifulSoup(html,'lxml')
    print(soup.prettify())
```


## 4个常用的对象
+ Beautiful Soup 将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种
+ 1. **Tag**：BeautifulSoup中所有的标签都是Tag类型，并且BeautifulSoup的对象其实本质上也是一个Tag类型。所以其实一些方法比如find、find_all并不是BeautifulSoup的，而是Tag的。
+ 2. **NavigableString**：继承自python中的str，用起来就跟使用python的str是一样的。
+ 3. **BeautifulSoup**：继承自Tag。用来生成BeaufifulSoup树的。对于一些查找方法，比如find、select这些，其实还是Tag的。
+ 4. **Comment**：这个也没什么好说，就是继承自NavigableString。

### 1. Tag:

+ Tag 通俗点讲就是HTML中的一个个标签，我们可以利用 soup加标签名，轻松地获取这些标签的内容
+ 这些对象的类型是 `<class 'bs4.element.Tag'>`
+ 注意，`soup.a` 查找的是所有内容中的第一个符合要求的标签

```python
type(soup.p)
<class 'bs4.element.Tag'>
soup.p
<p class="title" name="dromouse"></p>
soup.p.name
'p'
soup.p.attrs
{'class': ['title'], 'name': 'dromouse'}
soup.p.attrs['class']
['title']
soup.p['class']
['title']
soup.p.attrs.get('class')
['title']
soup.p.get('class')
['title']
soup.p['class'] = 'new'
soup.p
<p class="new" name="dromouse"></p>
class Tag(PageElement):
    """Represents an HTML or XML tag that is part of a parse tree, along
    with its attributes and contents.

    When Beautiful Soup parses the markup <b>penguin</b>, it will
    create a Tag object representing the <b> tag.
    """
    def get(self, key, default=None):
        """Returns the value of the 'key' attribute for the tag, or
        the value given for 'default' if it doesn't have that
        attribute."""
        return self.attrs.get(key, default)
```


### 2.  NavigableString:
+ 如果拿到标签 tag 后，还想获取tag 中的内容，那么可以通过 `tag.string` 获取 `tag`中的文字

```python
class NavigableString(str, PageElement):
    """A Python Unicode string that is part of a parse tree.

    When Beautiful Soup parses the markup <b>penguin</b>, it will
    create a NavigableString for the string "penguin".
    """   
    pass
soup.title
<title>The Dormouse's story</title>
soup.title.string
"The Dormouse's story"
type(soup.title.string)
<class 'bs4.element.NavigableString'>
```

### 3. BeautifulSoup

+ `BeautifulSoup` 继承自`Tag`
```python
class BeautifulSoup(Tag):
    """A data structure representing a parsed HTML or XML document.

    Most of the methods you'll call on a BeautifulSoup object are inherited from
    PageElement or Tag."""
    pass
```
+ `BeautifulSoup` 对象表示的是一个文档的全部内容，大部分时候可以把它当做Tag对象
+ 它支持遍历文档树和搜索文档树中描述的大部分的方法

### 4. Comment:

+ `Tag , NavigableString , BeautifulSoup` 几乎覆盖了html和xml中的所有内容,但是还
有一些特殊对象.容易让人担心的内容是文档的注释部分
Comment 对象是一个特殊类型的 NavigableString 对象

```python
class PreformattedString(NavigableString):
    """A NavigableString not subject to the normal formatting rules.

    This is an abstract class used for special kinds of strings such
    as comments (the Comment class) and CDATA blocks (the CData
    class).
    """
    
    PREFIX = ''
    SUFFIX = ''
class Comment(PreformattedString):
    """An HTML or XML comment."""
    PREFIX = '<!--'
    SUFFIX = '-->'
```


## 遍历文档树

### contents,children,descendants 属性


+ `contents`:返回所有**子节点的 列表**
+ `children`:返回所有子**节点的 迭代器**
+ `descendants`:返回所有**子孙节点的 迭代器**


### string,strings,stripped_strings 属性 以及get_text()方法
        
+ `string`:
    - 如果此元素有一个子字符串，则返回值为该字符串;
    - 如果此元素有一个子标签(tag)，则返回值是子标签(tag)的“string”属性（递归）;
    - 如果此元素~~**本身是字符串(bs4.element.NavigableString)**~~，没有子元素，或者有多个子元素，则返回值为None。
    ```python
    type(st.string)
    <class 'bs4.element.NavigableString'>
    st is st.string
    True
    ```
+ `strings`:
    - `_all_strings(self, strip=False, types=(NavigableString, CData))`
    - `strings = property(_all_strings)`
    - 返回某个**标签(tag)下的所有字符串的生成器**
+ `stripped_strings`:
    - `_all_strings(self, strip=False, types=(NavigableString, CData))`
    - `_all_strings(True)`
    - 返回某个**标签(tag)下的所有字符串的生成器(去掉空白字符;空行;头尾的空格,换行)**
+ `get_text(self, separator="", strip=False, types=(NavigableString, CData))`
    - `getText = get_text`
    - `text = property(get_text)`
    - 返回某个**标签(tag)下的所有字符串**

## find,find_all 方法

+ `find(name=None, attrs={}, recursive=True, text=None,**kwargs)`:
    - `find_all(name, attrs, recursive, text, 1, **kwargs)[0]`
    - 找到第一个满足条件的标签后就立即返回，只返回一个元素(tag)
+ `find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)`
    - 把所有满足条件的标签都选到，然后返回回去
    - 结果是`<class 'bs4.element.ResultSet'>`
    - `class ResultSet(list)`

### find_all 的使用

+ `attrs`:关键字参数或者attrs字典进行 标签(tag)的属性过滤
+ `limit`:限制提取 标签(tag)的数量

### 使用find和find_all的过滤条件：

1. **关键字参数**：将属性的名字作为关键字参数的名字，以及属性的值作为关键字参数的值进行过滤。
2. **`attrs`参数**：将属性条件放到一个字典中，传给attrs参数。


### 获取标签的属性：

+ **标签(tag) 的 attrs  属性是 字典**
  ```python
  type(p.attrs)
  <class 'dict'>
  ```

1. 通过下标获取：通过标签的下标的方式。

   ```python
   href = a['href']
   ```

2. 通过attrs属性获取：示例代码：

   ```python
   href = a.attrs['href']
   ```
3. 通过字典的get方法

    ```python
    href = a.attrs.get('href')
    ```  
   
## CSS选择器：

### select方法：

使用以上 `find` `find_all`方法可以方便的找出元素。但有时候使用`css`选择器的方式可以更加的方便。使用`css`选择器的语法，应该使用`select`方法。以下列出几种常用的`css`选择器方法：

#### （1）通过标签名查找：
+ 选择多个tag 用 逗号分隔
```python
print(soup.select('a'))
print(soup.select('title , a'))
```

#### （2）通过类名查找：

通过类名，则应该在类的前面加一个`.`。比如要查找`class=sister`的标签。示例代码如下：

```python
print(soup.select('.sister'))
```

#### （3）通过id查找：

通过id查找，应该在id的名字前面加一个＃号。示例代码如下：

```python
print(soup.select("#link1"))
```

#### （4）组合查找：

组合查找即和写 class 文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 等于 link1的内容，二者需要用空格分开：

```python
print(soup.select("p #link1"))
```

直接子标签查找，则使用 > 分隔：

```python
print(soup.select("head > title"))
```

#### （5）通过属性查找：

查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。示例代码如下：

```python
print(soup.select('a[href="http://example.com/elsie"]'))
pprint(soup.select('a#link2'))
```

#### （6）获取内容

以上的 select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
`getText=get_text`
`text = property(get_text)`
```python
soup = BeautifulSoup(html, 'lxml')
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())

for title in soup.select('title'):
    print(title.get_text())
```


#### （7）兄弟选择器
+ `+`:用于选择紧跟目标标签之后的第一个兄弟标签
+ `~`:会选择目标标签之后所有兄弟标签

```python
    rst = soup.select('p>#link1 + a')
    rst = soup.select('p>#link1 ~ a')
```

#### （8）按tag包含的内容选择

```python
    rst = soup.select('a:-soup-contains("some text")')
```







