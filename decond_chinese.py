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

print 'hello world'
