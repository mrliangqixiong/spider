from selenium import webdriver

driver = webdriver.Firefox()  # 创建一个webdriver对象
driver.implicitly_wait(15)
BASE_URL = 'http://www.zhaopin.com'
# 获取一页内容
driver.get(BASE_URL)
driver.find_element_by_id('KeyWord_kw2').send_keys('python')  # 输入python
driver.find_element_by_class_name('doSearch').click()  # 点击搜索

while True: 
    items = driver.find_elements_by_class_name("newlist")  # 获取所有item
    # 输出当前页中的所有item
    for item in items[1:]:
        print(item.text)

    # 如果有广告，关闭广告
    try:
        driver.find_element_by_class_name('closed_black_strip').click()
    except Exception as e:
        pass

    # 点击下一页，如果出现异常，break
    try:
        js = 'document.body.scrollTop="10000"'  # 定义要执行的js代码
        driver.execute_script(js)  # 执行js
        next_page = driver.find_element_by_class_name('next-page')  # 定位下一页元素
        next_page.click()  # 点击下一页
    except Exception as e:
        print(e)
        driver.get_screenshot_as_file("error.png")  #异常时，截屏
        break
