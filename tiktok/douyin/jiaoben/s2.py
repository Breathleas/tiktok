# -*- coding: utf-8 -*-#
# Name:         s2
# Description:  
# Author:       Wang Junling
# Date:         2019/11/25
from appium import webdriver
from time import sleep
from multiprocessing import Pool
import random
def run(port):
    desired_caps = {
                    'platformName': 'Android',
                    'deviceName': f'127.0.0.1:{port}',
                    # apk包名
                    'appPackage': 'com.ss.android.ugc.aweme',
                    # apk的launcherActivity
                    'appActivity': '.main.MainActivity',
                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    sleep(50)

    while True:
        sleep(1)
        try:
            print(port,driver.swipe(start_x=x*0.5,start_y=y*0.85,end_x=x*0.5,end_y=y*0.25))
        except Exception as a:
            print(a)

if __name__ == '__main__':
    list1=['52025']
    pool=Pool(10)
    for port in list1:
        print(f"开启{port}")
        pool.apply_async(run,args=(port,))
    pool.close()
    pool.join()

    print(f"结束")