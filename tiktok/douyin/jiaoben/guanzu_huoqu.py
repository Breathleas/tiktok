# -*- coding: utf-8 -*-#
# Name:         guanzu_huoqu
# Description:  
# Author:       Wang Junling
# Date:         2019/12/1
import logging
from appium import webdriver
from time import sleep
import random

def run(port):
    desired_caps = {
                    "platformName": "Android",
                    "noReset": True,
                    "autoAcceptAlerts": True,
                    "deviceName": "127.0.0.1:62025",
                    "appPackage": "com.ss.android.ugc.aweme",
                    "appActivity": ".main.MainActivity",

                    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    input("请移动到关注列表")
    # 设置华东次数，如果有新网红，可以在前面添加。
    dict1={r'穆雷中财':20,r'星悦小美女PKU':30,r'口语老炮儿马思瑞':30,
           r'万国土特产':20,r'夏波波Brian':50,r'西班牙小哥儿德明':20,
           '歪果仁研究协会':50,r'贝乐泰':15}
    num=272
    # jishu = 0
    # while True:
    #     driver.swipe(305,616, 305,497)
    #     sleep(5)

    # while jishu> len(dict1):
    for user in dict1.keys():
        sleep(random.randint (2,4))

        try:
            # 0号机器
            driver.tap([(104,num), (202, num+20)], 100)
            print(user)
            for i in range(dict1[user]):
                sleep(random.uniform(1,2))
                try:
                    driver.swipe(start_x=x * 0.5, start_y=y * 0.85, end_x=x * 0.5, end_y=y * 0.25)
                except Exception as a:
                    print(a)
        except Exception as a:
            print(user,a)
        driver.back()
        num += 113.5

if __name__ == "__main__":
    run("62001")
    print(f"结束")