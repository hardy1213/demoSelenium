# -*- coding:utf-8 -*-
import sys
from lib2to3.pgen2.driver import Driver
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Page(object):
    '''
    基础类，用于页面对象类的 
    '''
    login_url = 'http://www.163.com' #定义登录的URL地址
    
    def __init__(self, selenium_driver, base_url=login_url):  #定义初始化构造函数，传递两个参数
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        
    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)
    
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s ' %url
        
    def open(self):
        self._open(self.url)
        
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
    
class LoginPage(Page): #登录界面继承页面类page
    '''
    登录页面模型
    '''
    url = '/'
    
    #定位器用来定位用户名、密码
    username_loc = (By.ID, "idInput")
    password_loc = (By.ID, "pwdInput")
    submit_loc = (By.ID, "loginBtn") #提交按钮
    
    #Action
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)
        
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)
    
    def submit(self):
        self.find_element(*self.submit_loc).click()
    
def test_user_login(self, driver, username, password):
    '''
        测试获取的用户名和密码是否可以登录
    '''
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
        
def main(self):
    try:
        driver = webdriver.Firefox()
        username = 'username'
        password = 'password'
        test_user_login(driver, username, password)
        sleep(3)
        text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        assert(text == 'username@163.com',  "用户名称不匹配，登录失败！！！")
    finally:
        #关闭浏览器
        driver.close()

if __name__ == '__main__':
    main()
        
        
        
    
    
    
    
        
        
        
        
        
        
