from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

# 运行3秒后退出
time.sleep(3)
driver.quit()


