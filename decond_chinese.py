# -*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("seleniumm")

# ɾ��������һ��m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# ����ո��+�̳� "�̳�".decode("utf-8")�����UnicodeDecodeError: 'utf8' codec can't decode byte 0xe4
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("�̳�".decode("utf-8"))

# Ctrl+a ȫѡ����������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

# ��������������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

# ճ�����ݵ������
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

#ͨ���س��������浥������
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

#�˳������
driver.quit()