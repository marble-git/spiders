#--coding:utf-8--


import urllib
from urllib import request
response = request.urlopen('http://www.baidu.com')
print(response)
#print(response.read().decode('utf8'))
print(response.getcode())





