#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = '1193610322@qq.com'
receiver = '1193610322@qq.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '1193610322'
password = 'chenliyuanyang'
msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()