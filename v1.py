# coding: utf-8
from urllib import request, parse
from http import cookiejar
import time

#创建cookiejar实例
cookie = cookiejar.CookieJar()
#生成 cookiejar 管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handler = request.HTTPHandler()

#生成https 管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler,https_handler, cookie_handler)

#登录人人获取cookie
def login():
    url = 'http://www.renren.com/PLogin.do'
    data = {
            'email':'13119144223',
            'password':'123456'
            }

    #把数据进行编码
    data = parse.urlencode(data)
    req = request.Request(url,data=data.encode())
	#此处请求之后服务器端会设置cookie
    rsp = opener.open(req)

def getHomePage():
    url ='http://www.renren.com/965187997/profile'
    rsp = opener.open(url)
    with open('a.html','wb') as f:
        f.write(rsp.read())
		
#https://packagecontrol.io/Package%20Control.sublime-package
if __name__=='__main__':
    login()
    print(cookie)
    for item in cookie:
        print(item.domain)
        print(item.)
    time.sleep(2)
    getHomePage()

