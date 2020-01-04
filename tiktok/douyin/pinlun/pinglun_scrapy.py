# -*- coding: utf-8 -*-#
# Name:         s1
# Description:  
# Author:       Wang Junling
# Date:         2019/11/25
import logging
from appium import webdriver
from time import sleep
import os
from multiprocessing import Pool
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
    list1=[r'173259587',r'588429058',r'940546400'
        ,r'583875609',r'204826430',r'625754312'
           ]

    for user in list1:
        try:
            el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/aij")
            el3.send_keys(user)
            sleep(3)
            el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/aij")
            el3.click()


            driver.tap([(616, 1179), (629, 1244)], 100)


            sleep(10)

            # driver.tap([(616, 1179), (629, 1244)], 100)
            # driver.tap([(316,128), (362,163)], 100)
            # sleep(2)
            driver.tap([(174,289), (336,319)], 100)
            sleep(10)
            dict1={}
            num=0
            while True:
                sleep(random.uniform(0, 0.5))
                try:
                    if num == 30:
                        driver.swipe(start_x=x * 0.5, start_y=y * 0.55, end_x=x * 0.5, end_y=y * 0.75)
                        num = 0
                        cc = 0
                        for a, b, c in os.walk(r'D:\python\douyin\pinlun\pinglun_list'):
                            for file in c:
                                if dict1.get(file) != os.path.getmtime(a + '\\' + file):
                                    print(file, dict1.get(file), os.path.getmtime(a + '\\' + file))
                                    dict1[file] = os.path.getmtime(a + '\\' + file)
                                else:
                                    cc += 1
                            if cc == len(c):
                                print("下滑评论",
                                      driver.swipe(start_x=x * 0.5, start_y=y * 0.15, end_x=x * 0.5, end_y=y * 0.16))
                                sleep(1)
                                driver.swipe(start_x=x * 0.5, start_y=y * 0.85, end_x=x * 0.5, end_y=y * 0.25)
                                sleep(5)
                                try:
                                    driver.tap([(644, 851), (704, 911)], 100)
                                except Exception as a:
                                    sleep(1)
                                    driver.tap([(644, 851), (704, 911)], 100)
                                sleep(2)
                    else:
                        driver.swipe(start_x=x * 0.5, start_y=y * 0.80, end_x=x * 0.5, end_y=y * 0.30)
                        num += 1
                except Exception as err1:
                    print(err1)
        except Exception as err2:
            print(user,err2)
        driver.back()


if __name__ == "__main__":
    # pool=Pool(10)
    # for port in list1:
    #     print(f"开启{port}")
    #     pool.apply_async(run,args=(port,))
    # pool.close()
    # pool.join()
    run("62025")
    print(f"结束")