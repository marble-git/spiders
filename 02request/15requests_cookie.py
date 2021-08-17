# --coding-utf-8--

"""
    author  :   marble
    date    :   2021/8/17
    session : share cookie info
"""

import requests

# url = 'https://www.baidu.com'
url = 'https://www.zhihu.com/hot'
# headers = {
#     "user-agent": '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36''',
#     "cookie": '''_zap=64343eb7-cbe0-4439-875c-59ea06edf96a; d_c0="AGAU7TEViBKPTqrPu5aNSfsAOsZD5NXSFw4=|1611150006"; _xsrf=2c0caf82-a1ad-46ed-88df-b0d70165b8ab; l_n_c=1; n_c=1; q_c1=efeaadc704a94cec915694979bb88926|1615637505000|1612967180000; __snaker__id=BTbOnucyDqqpMUW7; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=5j%2F%2FDg%2BiUyRABRRURAJ%2Bnw9AsMIthaS7; tshl=; gdxidpyhxdE=y%5CDpa8nO9cVLW3v6oZ2g1y%5CD2LkHe94BVAAusj1ukqIfObN0srs%2B0LxgnUaAW7Z63GoOgISZZ85ErV9gQ2P1saJUbee1%2FlL%5C7A7VYkRtS1%2FLXh7cBYuUkWfgxfX03Qm2HabVTeVGNU6iP87c4oZfHZCodLWAbyI78dBt%5Cl3nCmEhiDDd%3A1628809125074; YD00517437729195%3AWM_NI=hyIfP6QXc%2BYe%2B2eKaDn7%2F2VrgwTlO9WMgyD%2BDh30tUilq6KhDV6TL5uFjV315F5lbmyys6dZz6n5KD8ET5TibfPxc5UZiY0%2FnvOTzDe1bKDlKlsmx4179puNtRzLTNGOdnc%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea6bb7bb28dbdd6b37df5bc8eb3d85e928e8faff463f3eaac95e742ad8f9ad0d02af0fea7c3b92aaca78787d33e9388adccdc6fe9eeabace450aee9e1d3d57aa5a99c8dce339593a99ac72188b8fdd1f75fabb4bfd7ca64888afab5cf3fb79aa6b7b23bf79afb8de167bba7bdd7e752baeaa2d6ca50fc9b9cd6d763a2baa099e23f9786a7bab325aeaa81b5f950a7efaeacc76889b4bd8efb40f3e9f791f846b88eb6add7468591ac8fe237e2a3; captcha_session_v2="2|1:0|10:1628778940|18:captcha_session_v2|88:emNxVjhaeUVUMmVRbFJvdS9NakFMOHkrU01FMkpOYmNScnMzdm80Y2xwdE5uaUFJK0J5WDFBSnJjU242OUYwcA==|60c9039218c8377cbd69c4b9737be9d593169bd80b1a463cef2f6feb14b1c2b4"; captcha_ticket_v2="2|1:0|10:1628778969|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfOGFQQmVQLUtNc0Q3cmlfMngtWUljV0xvZzFjakZKOXEyMFAtYnRQNmRrTnpoZDdsMFluVl9NRHpWUGpIMl9vVkVKQkVTTVJFRUdmY01LVDdKZm54eVhvNEpaYXlGRi5MLWZhZy1jWVU2RTd4RU9vLXdMQTlrZnpxLWpxcGljbkh4RlpCLWd4SlVhekRwTDBPbWZGaklpcDZQMlNuVUVIanB3TDUub0s4bll3Vm1kX3FoVmlMOGFJX1NrVFNPZUNZTi1IcnRaUERtZ0Z6aVZhY3pCS0x6SE1DQXZBREEwcFlSamZFQldqSjd5YjVZSmxsQmR3bnA3cW92X2VTaTk1eVdvOTlGWWp5amtCV3h3X0pFckFxdUxScDBQbDktWVg3Ti1nYW9PZ3RHU2VWNG84aUVuLVBJMUZ5YnlvRXNNaE4yQ1BPSURRWlU3cHN0azF1amxsNHpTLng1RzZaUFlYeTFta0JEX2dtRlRkaEM3cndURV9uUGZYT29XenU4di5pZzZHaE1yaFBMenpEbS5GZU5WdnJwdWl0Y2xfTFRmZVEueFg5bjE5RkU4VThLUGpWblFGWnhwSkJicFB6eXd4QnJpQ1JqX2t0cjlfNGxDdERCT3MyUHlITnBXOFJyWTlSTS1kTnJ0cmxBZjZVTVhBVEpPdkEyYVEtS0RTMyJ9|05f873e1d20c598582ed546bbac8f039f4b9db2a783a4644d3efdd5a74e7d7bd"; z_c0="2|1:0|10:1628778970|4:z_c0|92:Mi4xRnNCLUdRQUFBQUFBWUJUdE1SV0lFaVlBQUFCZ0FsVk4ybjhDWWdBV2tQQ3ppNV96djZmTTM1b3Zfbk5UbHJwQmZR|b90d475c04a28957cced21744f150486d518b56ab4806242147d077079bd15f3"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1628282282,1628292628,1628635882,1628980860; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1629157413; SESSIONID=VVsjhuWY8gSeysWhnu01AJwjKtqQpfrjCD0sc4CZwWE; KLBRSID=53650870f91603bc3193342a80cf198c|1629128076|1629128067; JOID=VV8dAU4LP8QxjtXSZg5dWajExVh7XWa9XOSgijUxWJhe8KSFAYi_01WM2tdrBT6WYkUj8m9TjUbyOELI8YBFHB8=; osd=UFAWBkIOMM82gtDdbQlRXKfPwlR-Um26UOGvgTI9XZdV96iADoO431CD0dBnADGdZUkm_WRUgUP9M0XE9I9OGxM=''',
# }
if __name__ == "__main__":
    # response = requests.get(url=url)
    # print(response)
    # print(response.cookies)
    # print(response.cookies.get_dict())
    # response = requests.get(url=url, headers=headers)
    # print(response.text)

    #1 login
    post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F'
    post_data = {
        'username': '1097566154@qq.com',
        'password': 'wq15290884759.'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    session = requests.session()
    session.post(url=post_url,data=post_data,headers=headers)
    #2 access personal web
    personal_url = 'https://i.meishi.cc/cook.php?id=13686422'
    response = session.get(url=personal_url,headers=headers)
    print(response.text)
    print(response.cookies)
    print(response.cookies.get_dict())
    print(response.json())
    pass
