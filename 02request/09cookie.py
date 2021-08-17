# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/11
    模拟登录知乎
"""

import urllib
from urllib import request

url = "http://www.zhihu.com/hot"

headers = {
    "cookie": """_zap=64343eb7-cbe0-4439-875c-59ea06edf96a; d_c0="AGAU7TEViBKPTqrPu5aNSfsAOsZD5NXSFw4=|1611150006"; 
    _xsrf=2c0caf82-a1ad-46ed-88df-b0d70165b8ab; l_n_c=1; n_c=1; 
    q_c1=efeaadc704a94cec915694979bb88926|1615637505000|1612967180000; 
    Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1627253239,1628282282,1628292628,1628635882; 
    captcha_session_v2="2|1:0|10:1628611099|18:captcha_session_v2|88 
    :dVRkU1dZVnQ4b0VBZmN4bTBRa1pVSFFhSlUwOWJaR0xvSlFycDFzRzZtREtUWm1PK1pNS0VTbHpDT3VnMjNYcA 
    ==|d29ff98ee2f9a8556c95b61880e08558373eee674ff25be231f4d6f834c8c35d"; 
    SESSIONID=Fk9rKJaYcjKJErgYY8NXqCddaEC11Fze2qM61cEjvgB; __snaker__id=BTbOnucyDqqpMUW7; 
    JOID=V1EQBUlcbtqPUmvfel8FSBwSfVxoFgng-R4tsiA4CJ3GEx60L37Dz-1Za9B9NycX7PpxCmxRGmJ4tQ4AnV__cZ0=; 
    osd=UlAdBEJZb9eOWW7ed14OTR0ffFdtFwTh8hssvyEzDZzLEhWxLnPCxOhYZtF2MiYa7fF0C2FQEWd5uA8LmF7ycJY=; 
    gdxidpyhxdE=jg9bDpJQXaZ%2Bz5xu%2BdvHeactGZPAk9fLQZ1ov%2BhmTj89s9bj8h2RxIE238mez%2BikeOlgedNaUEBl3n6roeHLvhi 
    %2Bx0yITZHViy%5CKEwLnuR6aLLH96fdrM4RRqkXvsVLN1NTBclsD%5C05DGQms2LGDec0AXm6UHlGX3ncm2SRLUgWzOm9%5C%3A1628641349657 
    ; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=BsrmJWKJHfx6VdwRDfYRB%2BYUwtJdKj4QyvCLT8751CvQFy4OBrW1mmsCtqpLz 
    %2FwPtKsRH2hbmle4eriJAiga09JsHYG53wmhJjFGJXEuk0PlfIaZ%2BZCbsR0QAR37Pm5yVk4%3D; YD00517437729195%3AWM_NIKE 
    =9ca17ae2e6ffcda170e2e6eeb7c43f82948ed4f161b6eb8ab6d15f929a9bbbf473b0e89fd9e243b4b985b9b52af0fea7c3b92a82adbe8ec95d89968887fb3e96bcb9b3c76e9b8e8eccdc5fb5ac8685ca62f88fb797c24898e8f9d6b449b68f8a9ab74582ae99d2f067b19dbc92f348baf1b9b1f741b18e88d3eb6aafb4abd5e87aab968f8ae66bf4e78694cb5385ebfd98f0648ab68aa8c95487aba5d1d368a697afbbaa5281bebdb3b35b838efdd8d367f7a79a8cb737e2a3; YD00517437729195%3AWM_TID=5j%2F%2FDg%2BiUyRABRRURAJ%2Bnw9AsMIthaS7; z_c0="2|1:0|10:1628611154|4:z_c0|92:Mi4xRnNCLUdRQUFBQUFBWUJUdE1SV0lFaWNBQUFDRUFsVk5VaTg2WVFBbVdIa193NXNqQW5qNVdmY3NXTTNWdDNmUGl3|b829f69ea25632001e8588c5921c5efdcf553ca92c0eb37b83fcd2de42c7674e"; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1628640500; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1628611339|1628611092 """
}

# response = request.urlopen(url)
rq = request.Request(url, headers=headers)
response = request.urlopen(rq)
print(response.read().decode('utf8'))

if __name__ == "__main__":
    pass
