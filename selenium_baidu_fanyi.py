from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get('http://fanyi.baidu.com/translate#zh/en/')

ele = driver.find_element_by_xpath("//textarea[@class='textarea']")
ele.send_keys("你好")

time.sleep(3)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

time.sleep(2)
driver.quit()
