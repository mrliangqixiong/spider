from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get('http://www.baidu.com')

# driver.save_screenshot("baidu.png")
# print( driver.page_source )
# with open("baidu.html", 'w', encoding='utf8') as f:
#    f.write(driver.page_source)

ele = driver.find_element_by_xpath("//input[@id='kw']")
ele.send_keys("美女")

ele = driver.find_element_by_xpath("//input[@id='su']")
ele.click()

time.sleep(3)
driver.quit()
