# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 16:48
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : Regularly_update.py
# @Software: PyCharm

import logging
import os
import json
import random
import shutil
import pymysql
from appium import webdriver
from time import sleep



LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='TikTok.log', filemode='a', )


class TikTok(object):
    """

    """

    def __init__(self):

        # self.user = {
        #     '穆雷中财': 15,
        #     '星悦小美女PKU': 30,
        #     '口语老炮儿马思瑞': 30,
        #     '万国土特产': 20,
        #     '夏波波Brian': 50,
        #     '西班牙小哥儿德明': 20,
        #     '歪果仁研究协会': 50,
        #     '贝乐泰': 15
        # }
        self.user_id = {
            '穆雷中财': 86462745631,
            '贝乐泰': 98492270062,
            '歪果仁研究协会': 84838275326,
            '西班牙小哥儿德明': 95040145160,
            '夏波波Brian': 80745032657,
            '万国土特产': 95353972682,
            '口语老炮儿马思瑞': 68001314839,
            '星悦小美女PKU': 82837571567,
            '俏奶奶二人组': 68354827719,
            '大静奋斗ing': 2334997990873038,
            '好获严选': 3003501057414974,
        }
        self.user = {
            '穆雷中财': 15,
            '贝乐泰': 15,
            '歪果仁研究协会': 50,
            '西班牙小哥儿德明': 20,
            '夏波波Brian': 50,
            '万国土特产': 20,
            '口语老炮儿马思瑞': 30,
            '星悦小美女PKU': 30,
            '俏奶奶二人组': 2,
            '大静奋斗ing': 2,
            '好获严选': 2
        }
        self.user_search_id = {
            '穆雷中财': 204826430,
            '贝乐泰': 940546400,
            '歪果仁研究协会': 588429058,
            '西班牙小哥儿德明': 583875609,
            '夏波波Brian': 'LYLC',
            '万国土特产': 625754312,
            '口语老炮儿马思瑞': 'yingyuzhidao',
            '星悦小美女PKU': 173259587,
            '俏奶奶二人组': 'ayimeizhuang',
            '大静奋斗ing': 'mengdajing',
            '好获严选': 'dyrxy0sv2ryr',
        }
        self.setting = {
            "platformName": "Android",
            "noReset": True,
            "autoAcceptAlerts": True,
            "deviceName": "127.0.0.1:62025",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            "unicodekeyboard": True,
            "resetKeyboard":True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.setting)
        self.x = self.driver.get_window_size()["width"]
        self.y = self.driver.get_window_size()["height"]
    def click_home(self):
        while True:
            try:
                self.driver.tap([(636, 1219), (659, 1253)], 100)
                break
            except Exception as err:
                logging.error(err)
        sleep(3)
        while True:
            try:
                el1 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aq8")
                el1.click()
                break
            except Exception as err:
                logging.error(err)

    def click_comment(self):
        while True:
            try:
                self.driver.tap([(674, 854), (678, 880)], 100)
                break
            except Exception as err:
                logging.error(err)

    def click(self, coordinate):
        while True:
            try:
                self.driver.tap(coordinate, 100)
                break
            except Exception as err:
                logging.error(err)

    def del_file(self):

        for path in self.path_list:
            path = os.path.join(os.getcwd(), f'{path}')
            shutil.rmtree(path)
            os.mkdir(path)


    def get_updata(self):

        # input("Please move to the user concern list and hit enter to start.")
        sleep(10)
        num = 272
        flag = True
        while flag:
            flag = self.click_home()
        sleep(5)
        # self.del_file()

        # jishu = 0
        # while True:
        #     driver.swipe(305,616, 305,497)
        #     sleep(5)

        # while jishu> len(self.user):
        # try:
        #     self.driver.tap([(636, 1219), (659, 1253)], 100)
        #     self.driver.tap([(636, 1219), (659, 1253)], 100)
        #     self.driver.tap([(636, 1219), (659, 1253)], 100)
        # except

        for user in self.user.keys():
            try:
                print(user)
                while True:
                    try:
                        el1 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aia")
                        el1.click()
                        el1.send_keys(self.user_search_id[user])
                        break
                    except Exception as err:
                        pass
                sleep(1)
                self.driver.tap([(104, 272), (202, 272 + 20)])
                sleep(5)
                self.driver.back()



            except Exception as a:
                logging.error(f'{user, a}')
                self.driver.back()

if __name__ == '__main__':
    # while True:
    #     run = TikTok()
    #     run.get_updata()
    #     sleep(30)
    print(dir(TikTok))


# el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]")
# el4.click()