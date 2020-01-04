# -*- coding: utf-8 -*-#
# Name:         s1
# Description:  
# Author:       Wang Junling
# Date:         2019/11/25
import logging
from appium import webdriver
from time import sleep
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

            for i in range(70):
                sleep(random.uniform(1, 2))
                try:
                    print(port, driver.swipe(start_x=x * 0.5, start_y=y * 0.85, end_x=x * 0.5, end_y=y * 0.25))
                except Exception as a:
                    print(a)
        except Exception as a:
            print(user,a)
        driver.back()
    # el3=driver.find_element_by_id("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout")
    # print(el3)
    # while True:
    #     sleep(1)
    #     try:
    #         print(port,driver.swipe(start_x=x*0.5,start_y=y*0.85,end_x=x*0.5,end_y=y*0.25))
    #     except Exception as a:
    #         print(a)

if __name__ == "__main__":
    # pool=Pool(10)
    # for port in list1:
    #     print(f"开启{port}")
    #     pool.apply_async(run,args=(port,))
    # pool.close()
    # pool.join()
    run("62025")
    print(f"结束")