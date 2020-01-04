# -*- coding: utf-8 -*-#
# Name:         script
# Description:  该脚本是用来获取每条发布的评论的信息。前置需要登陆抖音，搜索网红，进入一个网红的发布，点击评论，在脚本中敲击回车键，就ok了。
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
    el1=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.DmtViewPager.MyAccessibilityDelegate/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
    el1.click()
    el2 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/c08")
    el2.click()

    el3 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/cfy")
    el3.send_keys("")
    el4 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/cen")

    el4.send_keys("")

    el5 = driver.find_element_by_id("com.ss.android.ugc.aweme:id/cou")
    el5.click()
    el6 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.LinearLayout[2]/android.widget.LinearLayout")
    el6.click()

    input('请登录后回车继续运行')
    dict1 = {}

    while True:
        sleep(random.uniform(0,0.5))
        try:
            if num == 30:
                driver.swipe(start_x=x * 0.5, start_y=y * 0.55, end_x=x * 0.5, end_y=y * 0.75)
                num = 0
                cc = 0
                for a, b, c in os.walk(r'D:\python\douyin\pinlun\pinglun_list'):
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
    run('62025')
    print(f"结束")
