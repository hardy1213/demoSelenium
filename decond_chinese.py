# -*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm")

# 删除输入框的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键+教程 "教程".decode("utf-8")解决了UnicodeDecodeError: 'utf8' codec can't decode byte 0xe4
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程".decode("utf-8"))

# Ctrl+a 全选输入框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# 剪切输入框的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

#通过回车键来代替单击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

#退出浏览器
driver.quit()

#如何发送邮件？
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#定义发送邮箱的服务器
smtpserver = 'smtp.163.com'

#定义发送邮箱的用户名、密码
user = '************'
password = '******'

#发送的邮箱
sender = '*************'

#定义接受的邮箱，第一种方法：列表接收
receiver = ['***************','********']

#第二种方法：邮件存到TXT文件中，直接修改
'''
receiver = open('D:\\b.txt','r')
lines = receiver.readlines() #每次读取一行
receiver = [] #定义一个空列表
for line in lines:
    receiver.append(line.replace("\n","")) #拼接
 '''   
#发送邮件主题
subject =  'python email test'

#发送邮件的正文
msg = MIMEText('<html><h1>test python</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
                                 
#连接发送邮件
smtp = smtplib.SMTP()   
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

#如何发送带附件的邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#发送邮箱的服务器
smtpserver = 'smtp.163.com'

#发送邮箱的用户名、密码
user = 'fengjikun1987@163.com'
password = 'fengJK1986526' #此密码不是邮箱密码，是邮箱代理的密码

#发送的邮箱
sender = 'fengjikun1987@163.com'

#接收的邮箱，具体方法参考上面发送邮箱的方法
receiver = ['xxxxxxx','xxxxxxxxxxxxxxxxxx']

#发送邮件主题
subject = 'Python send attach email'

#发送的附件 sendfile = open("wangyu.jpg", 'rb').read()如果不写路径，默认为当前的路径下
sendfile = open("D:\\selenium.png",'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="Selenium.png"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
