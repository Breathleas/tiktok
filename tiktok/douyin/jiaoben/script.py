# -*- coding: utf-8 -*-#
# Name:         script
# Description:  
# Author:       Wang Junling
# Date:         2019/11/23
from appium import webdriver
from time import sleep
from multiprocessing import Pool
import random
import os
def run(port):
    num=0
    desired_caps = {
                    'platformName': 'Android',
                    'deviceName': f'127.0.0.1:{port}',
                    # apk包名
                    'appPackage': 'com.ss.android.ugc.aweme',
                    # apk的launcherActivity
                    'appActivity': '.main.MainActivity',
                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    input('请登录后回车继续运行')
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    # driver.navigate().back()
    dict1 = {}
    while True:
        sleep(random.uniform(0,0.5))
        try:
            if num == 30:
                driver.swipe(start_x=x * 0.5, start_y=y * 0.55, end_x=x * 0.5, end_y=y * 0.75)
                num = 0
                cc = 0
                for a, b, c in os.walk('E:\\fabu'):
                    for file in c:
                        if dict1.get(file) != os.path.getmtime(a + '\\' + file):
                            print(file,dict1.get(file),os.path.getmtime(a + '\\' + file))
                            dict1[file] = os.path.getmtime(a + '\\' + file)
                        else:
                            cc += 1
                    if cc == len(c):
                        print("下滑评论", driver.swipe(start_x=x * 0.5, start_y=y *0.15 , end_x=x * 0.5, end_y=y * 0.16))
                        sleep(1)
                        driver.swipe(start_x=x * 0.5, start_y=y *0.85, end_x=x * 0.5, end_y=y *0.25 )
                        sleep(5)
                        try:
                            driver.tap([(644,851),(704,911)], 100)
                        except Exception as a:
                            sleep(1)
                            driver.tap([(644, 851), (704, 911)], 100)
                        sleep(2)
            else:
                driver.swipe(start_x=x*0.5,start_y=y*0.80,end_x=x*0.5,end_y=y*0.30)
                num += 1
        except Exception as a:
            print(a)

if __name__ == '__main__':
    list1=['62025']
    # pool=Pool(10)
    # for port in list1:
    #     print(f"开启{port}")
    #     pool.apply_async(run,args=(port,))
    # pool.close()
    # pool.join()

    run('62025')
    print(f"结束")
