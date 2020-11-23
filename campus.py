import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

username = "19138919564"
passwd = "11292415"
# browser = webdriver.Chrome()
# 实例化一个启动参数对象
chrome_options = Options()
# # # # 设置浏览器窗口大小
# # # # chrome_options.add_argument('--window-size=136,76')--profile-directory="Profile 1"
# # # # chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=330,170')
# path = r"C:\Users\16966\AppData\Local\Google\Chrome\User Data\Default"
# chrome_options.add_argument('--user-data-dir="C:\\Users\\16966\\AppData\\Local\\Google\\Chrome"')
# # 启动浏览器chrome_options=chrome_options
browser = webdriver.Chrome(chrome_options=chrome_options)
while True:

    try:
        browser.get("http://192.168.189.136/eportal/index.jsp?wlanuserip=5a5ce9e3301c04431ec045431dd91408&wlanacname"
                    "=c49acf9a4ee3cd0a&ssid=32af29c6e99b1e87&nasip=0aaf6f129fc7a39e46eba82633ad7b2f&mac"
                    "=01e1b9f563119ddab35850ec660d84c7&t=wireless-v2&url"
                    "=4124e53662e4205944a29786438aef8f2f6feb21795ee7fb")
        # browser.implicitly_wait(1000)
        time.sleep(2)
        a = browser.find_element_by_id("username_tip")
        a.send_keys(username, Keys.TAB)
        print("账户输入成功")
        time.sleep(2)
        b = browser.find_element_by_id("pwd")
        b.send_keys(passwd)
        print("密码输入成功")
        time.sleep(2)
        # browser.implicitly_wait(1000)
        # a = browser.find_element_by_id("login_btn_1")
        # a.click()
        browser.execute_script("return doauthen()")
        print("登录成功")
        time.sleep(2)
    except:
        print("未掉线重复登录成功")
        pass
    time.sleep(200)
print("登录完成-两秒后关闭浏览器")
time.sleep(2)
browser.close()
print("关闭浏览器成功")
print()
time.sleep(200)
