from selenium import webdriver
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('D:/ProgramFiles/phantomjs-2.1.1-windows/bin/phantomjs.exe')

driver.get('https://www.zhihu.com/signup?next=%2F')
time.sleep(2)

cookies = {
'_xsrf' : 'ec31e5ef-38f1-496c-a138-4fa98ef1b37a',
'q_c1' : '6212bd9babee471e9a2f0e7cb35b0fd7|1519978056000|1519978056000',
'_zap' : 'f921c2b7-f8ab-419b-8572-4372cc5fa67f',
'd_c0' : 'AIBrfN6DOQ2PToc4khtp8ItgYD8sMUa31cA=|1519978073',
'capsion_ticket' : '2|1:0|10:1519979001|14:capsion_ticket|44:MTIzOTc5NGJjMjVkNGM3MDkwYzUzZmI0YTVkZDQ2NTI=|7031598f27ae1ceb707b309f30f064de6d6c8c0047710a8dee2f170cac9a2faf',
'z_c0' : '2|1:0|10:1519979007|4:z_c0|92:Mi4xYm4wY0FRQUFBQUFBZ0d0ODNvTTVEU1lBQUFCZ0FsVk5fMWVHV3dBT2hCaEZ6VkhleTRwX2dvWUFZYVZmWjQ1SFZB|351ee192a4c13ff3162b6f2209f32197e2110c9778ed52212e449959107d6931',
}

driver.add_cookie({'domain':'www.zhihu.com',
                   'name':'aliyungf_tc',
                   'value':'AQAAAAT+mX/BaQoAuF5ccY/yw/q2GFxZ'})

for k, v in cookies.items():
    one_cookie = {'domain':'.zhihu.com', 'name':k, 'value':v}
    driver.add_cookie(one_cookie)

time.sleep(1)

driver.get("https://www.zhihu.com/")

time.sleep(6)
# driver.save_screenshot('zhihu.png')
driver.quit()


