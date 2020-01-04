# -*- coding: utf-8 -*-#
# Name:         s1
# Description:  
# Author:       Wang Junling
# Date:         2019/11/25
import logging
from appium import webdriver
from time import sleep
import random

def run(port):
    desired_caps = {
                    "platformName": "Android",
                    "deviceName": "127.0.0.1:62025",
                    "appPackage": "com.ss.android.ugc.aweme",
                    "appActivity": ".main.MainActivity"
                    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    input("sss")
    # r'LYLC', r'yingyuzhidao',
    driver.tap([(9, 44), (63, 98)], 100)
    list1={r'yingyuzhidao':20,r'LYLC':50,r'583875609':30,
           r'173259587':30,r'204826430':30,r'588429058':30,
           r'940546400':15}

    for user in list1.keys():

        try:
            # 0号机器
            driver.tap([(134, 56), (303, 87)], 100)

            el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/aia")
            el3.send_keys(user)
            # print(user)

            # 1号机器
            # 单机输入框
            # el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/aij")
            # el3.click()
            # # 输入内容
            # sleep(2)
            # el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/aij")
            # el3.send_keys(user)


            sleep(5)

            # 回车
            driver.keyevent(66)
            sleep(2)
            driver.keyevent(66)
            sleep(3)


            driver.tap([(316,128), (362,163)], 100)


            sleep(3)

            driver.tap([(134, 56), (303, 87)], 100)


            driver.keyevent(66)
            sleep(2)
            driver.keyevent(66)
            sleep(2)
            driver.keyevent(66)


            sleep(10)

            driver.tap([(207,202), (384,219)], 100)
            sleep(5)

            for i in range(list1[user]):
                sleep(random.uniform(1,2))
                try:
                    port, driver.swipe(start_x=x * 0.5, start_y=y * 0.85, end_x=x * 0.5, end_y=y * 0.25)
                except Exception as a:
                    print(a)
        except Exception as a:
            print(user,a)
        driver.back()

if __name__ == "__main__":

    run("62001")
    print(f"结束")