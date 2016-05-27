# -*- coding: utf-8 -*-
import http.cookiejar as cookielib
import urllib
import urllib
import re

url_login = 'http://f.10086.cn/im/login/inputpasssubmit1.action'
url_logout = 'http://f.10086.cn//im/index/logoutsubmit.action?t='
url_msg = 'http://f.10086.cn/im/user/sendMsgToMyselfs.action'
user = '15957120592'
password = 'chenyang'
loginstatus = '4' 
arg_t = ''

def fetion(msg):
    cj = cookielib.LWPCookieJar()
    opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
    urllib.install_opener(opener)
    args = {'pass':password, 'm':user,'loginstatus':loginstatus}
    print ('Logining...')
    req = urllib.Request(url_login, urllib.urlencode(args))
    jump = opener.open(req)
    page = jump.read();
    url = re.compile(r'<card id="start".*?ontimer="(.*?);').findall(page)[0]             #��ȡ��ת����
    arg_t = re.compile(r't=(\d*)').findall(page)[0]
    if url == '/im/login/login.action':                                                   #��¼ʧ��
        print('Login Failed!')
        input('Press any key to exit.')
        return
    else:
        print('Login Successfully!')
    sendmsg = urllib.Request(url_msg, urllib.urlencode({'msg':msg.decode('gbk').encode('utf-8')}))
    finish = urllib.urlopen(sendmsg)

    if finish.geturl == 'http://f.10086.cn/im/user/sendMsgToMyself.action' :
        print('Send Failed!')
    else:
        print('Send Successfully')
    logout = urllib.Request(url_logout + arg_t)
    response = urllib.urlopen(logout)                                                    #ע��
    print('Logout Successfully!')
    #print response.read().decode('utf-8').encode('gbk')

msg = input('what do you want to say:')
fetion(msg)