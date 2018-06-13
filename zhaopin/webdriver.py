from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 1秒后运行
driver.implicitly_wait(1)
driver.get('https://www.baidu.com')

#  把a拖到b所在的位置
a =driver.find_element_by_id('kw')
b = driver.find_element_by_id('su')

# 双击b元素
# ActionChains(driver).double_click(b).perform()

# 移动鼠标到b上
ActionChains(driver).move_to_element(b).perform()

# 右键单击b元素
ActionChains(driver).context_click(b).perform()
time.sleep(5)
# 把a拖到b上
ActionChains(driver).drag_and_drop(a,b).perform()

driver.quit()






















