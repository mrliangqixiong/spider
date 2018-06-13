from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get('https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=')
time.sleep(2)

ele = driver.find_element_by_id('loginName')
ele.send_keys('xxxxx@163.com')

ele = driver.find_element_by_id('loginPassword')
ele.send_keys('xxxxx')

ele = driver.find_element_by_id("loginAction")
ele.click()

time.sleep(5)
driver.save_screenshot('weibo.png')
driver.quit()


