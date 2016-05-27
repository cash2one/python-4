# coding=UTF-8

import urllib;
import  urllib.parse;
from http.cookiejar import MozillaCookieJar
import urllib.request;
from urllib.error import HTTPError,URLError

head={"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
      "accept-language":"zh-CN,zh;q=0.8"};
data = {};
daili={"http":"http://27.115.75.114:8080"};
# daili={};
#daili = {'http':"http://192.168.1.1:80"}

proxy_support = urllib.request.ProxyHandler(daili);

#声明一个CookieJar对象实例来保存cookie
cookie = MozillaCookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler,urllib.request.HTTPHandler);
# 这个使用代理的  有可能会出错
# opener = urllib.request.build_opener(proxy_support,handler,urllib.request.HTTPHandler);
urllib.request.install_opener(opener);

head["user-agent"] ='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36';
# head['Accept-Language'] = 'zh-CN,zh;q=0.8';
# head['Accept-Encoding'] = 'gzip, deflate, sdch';
# head['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8';
# head['Host'] = '1212.ip138.com'
# head['Cookie'] = 'ASPSESSIONIDSSTSCSBB=KBHKAOODGPJNGPPNLHELAEPG'

data = urllib.parse.urlencode(data).encode("utf-8");
myurl = "http://www.ipshi.com/";
myurl = "http://www.w3school.com.cn/";

try:
      req = urllib.request.Request(url=myurl,data=None,headers=head);
#       HttpError 是URLError的子类
except HTTPError as e:

    print('The server couldn\'t fulfill the request.')

    print ('Error code: ', e.code)

# 通常，URLError在没有网络连接(没有路由到特定服务器)，或者服务器不存在的情况下产生。
except URLError as e:

    print ('We failed to reach a server.')

    print ('Reason: ', e.reason)

else:
    print ('No exception was raised.')
    # everything is fine
# req.set_proxy("120.195.205.131:80","http");
response = urllib.request.urlopen(req);

for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)
# 有时候会发生重定向 这时候可以使用 response.geturl()

nowUrl = response.geturl();
print(nowUrl)

html = response.read();
try:
      html = html.decode("utf-8");
except (Exception) as e:
      print(e)
      html = html.decode("gb2312");

# pattern  = re.compile("Your IP Address Is:\s{0,}<div>.{0,}");
# pattern1 = re.compile("&#\d{2,2}");
# html = pattern.findall(html);
# html = pattern1.findall(html);
# print(html);
