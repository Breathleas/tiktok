# -*- coding: utf-8 -*-#
# Name:         douyin_get
# Description:  整体douyin自动化爬虫脚本，需要appium\adb\mitmproxy\python3.6等安装包支持才可运行
# Author:       Wang Junling
# Date:         2019/12/2

import logging
import os
import random
import shutil
import pymysql
from appium import webdriver
from time import sleep
from multiprocessing import Pool

LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='TikTok.log', filemode='a', )


class TikTok(object):
    """
    抖音appium爬虫方法
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
        # 如果有新入的网红请修改这里
        self.user_search_id = {
            '口语老炮儿马思瑞': 'yingyuzhidao',
            '星悦小美女PKU': 173259587,
            '俏奶奶二人组': 'ayimeizhuang',
            '大静奋斗ing': 'mengdajing',
            '好获严选': 'dyrxy0sv2ryr',
            '穆雷中财': 204826430,
            '贝乐泰': 940546400,
            '歪果仁研究协会': 588429058,
            '西班牙小哥儿德明': 583875609,
            '夏波波Brian': 'LYLC',
            '万国土特产': 625754312,

        }
        # 与上一个文件相对饮，非常重要
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
        # 发布数量需要滑动几次
        self.user = {
            '口语老炮儿马思瑞': 30,
            '星悦小美女PKU': 30,
            '俏奶奶二人组': 2,
            '大静奋斗ing': 2,
            '好获严选': 2,
            '穆雷中财': 15,
            '贝乐泰': 15,
            '歪果仁研究协会': 50,
            '西班牙小哥儿德明': 20,
            '夏波波Brian': 50,
            '万国土特产': 20,

        }
        self.fabuliang = {'穆雷中财': 70,
                          '星悦小美女PKU': 135,
                          '口语老炮儿马思瑞': 120,
                          '万国土特产': 90,
                          '夏波波Brian': 370,
                          '西班牙小哥儿德明': 172,
                          '歪果仁研究协会': 285,
                          '贝乐泰': 30,
                          '俏奶奶二人组': 13,
                          '大静奋斗ing': 13,
                          '好获严选': 5
                          }

        self.setting = {
            "platformName": "Android",
            "noReset": True,
            "autoAcceptAlerts": True,
            "deviceName": "127.0.0.1:62025",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            "unicodekeyboard": True,
            "resetKeyboard": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.setting)
        self.x = self.driver.get_window_size()["width"]
        self.y = self.driver.get_window_size()["height"]

        self.path_list = [r'analysis\user', r'fabuxingxi\fabu_list']
        self.pinglun_path = 'pinlun\pinglun_list'
        self.fans_list = r'fans\fans_list'
        self.fans_user_list = r'fans\fans_user_list'

    def click_home(self):
        '''
        用来自动点击home
        :return:
        '''
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
        '''
        点起home件
        :return:
        '''
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

    def get_mysql(self, sql):

        connect = pymysql.connect(host='52.81.170.174',
                                  user='wangjunling',
                                  password='Wjl1314520.',
                                  db='tiktok',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)
        cursor = connect.cursor()
        cursor.execute(sql)
        cc = cursor.fetchall()
        cursor.close()
        connect.close()
        return cc

    def get_comment(self):

        flag = True
        while flag:
            flag = self.click_home()
        sleep(5)

        num = 0
        for user in self.user.keys():
            fanhui = 1
            # sleep(random.randint(2, 4))

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
                self.click([(104, 272), (202, 272 + 20)])
                sleep(5)

                self.click([(49, 994), (160, 1014)])
                sleep(2)
                self.click_comment()

                sleep(3)
                next_cc = 1
                while True:

                    # sleep(random.uniform(0, 0.2))
                    try:
                        if num == 10:
                            num = 0
                            sql = f"""select count(*) from tiktok_comment_tests"""
                            """
                            上面的sql是用来查询评论数据量是否在一定的时间内增加数据，如果没有增加数据，则换一条发布.
                            The above SQL is used to query whether the amount of comment data increases within a certain period of time. If there is no increase in data, then another one will be published.
                            fanhui：这个是用来统计发布量的，如果发布量到达一定区间，换下一个网红请求。
                                    This is used to count the number of publications. If the number of publications reaches a certain range, change the next web celebrity request.

                            """
                            cc = self.get_mysql(sql)
                            print(cc, next_cc)

                            if cc[0]['count(*)'] == next_cc:
                                print("下滑评论")
                                fanhui += 1
                                print(fanhui)

                                if fanhui > self.fabuliang[user]:
                                    self.driver.back()
                                    break

                                while True:
                                    try:
                                        print('点击')
                                        self.driver.tap([(305, 294), (310, 300)], 100)
                                        break
                                    except Exception as err:
                                        logging.error(err)

                                sleep(2)

                                while True:
                                    try:
                                        print('下滑')
                                        self.driver.swipe(start_x=self.x * 0.5,
                                                          start_y=self.y * 0.85,
                                                          end_x=self.x * 0.5,
                                                          end_y=self.y * 0.25)
                                        break
                                    except Exception as err:
                                        logging.error(err)

                                sleep(2)

                                self.click_comment()

                                sleep(2)
                            else:
                                next_cc = cc[0]['count(*)']
                        else:
                            while True:
                                try:
                                    self.driver.swipe(start_x=self.x * 0.5, start_y=self.y * 0.88, end_x=self.x * 0.5,
                                                      end_y=self.y * 0.35)
                                    break
                                except Exception as err:
                                    logging.error(err)
                            num += 1
                    except Exception as a:
                        print(a)
                self.driver.back()
                self.driver.back()

            except Exception as a:
                print(user, a)

    def get_fans(self):

        sql = f"""select fans_user_id,short_id,unique_id from tiktok.tiktok_fans_test where short_id!=0 and json_content like '[]' and user_id=84838275326"""
        """
        为拿到用户城市，从数据库中查出没有城市的用户，使用short_id或unique_id来搜索用户
        To get the user city, find users without a city from the database, use short_id or unique_id to search for the user
        从数据库中查出没有城市的用户，使用short_id或unique_id来搜索用户
        """

        # print(sql)
        datas = self.get_mysql(sql)
        # print(datas)
        # dict1 = {}
        while True:
            try:
                el1 = self.driver.find_element_by_accessibility_id("搜索")
                el1.click()
                break
            except Exception as err:
                pass

        for data in datas:
            print(data)
            try:
                el1 = self.driver.find_element_by_accessibility_id("搜索")
                el1.click()
            except Exception as err:
                pass
            # sleep(3)
            # # 一下语句需要修改，by_id会根据版本不一样，随机生成，如果安装的运行前最好检测每一个使用id定位的元素
            try:
                el2 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aia")
                el2.send_keys(data.get('short_id'))
            except Exception as err:
                self.driver.back()
                el2 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aia")
                el2.send_keys(data.get('unique_id'))

            sleep(2)
            self.click([(628, 1205), (686, 1230)])
            # self.driver.keyevent(66)
            sleep(6)
            # self.driver.press_keycode(84)
            # el1 = self.driver.find_element_by_xpath(
            #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[3]/android.widget.TextView")
            # el1.click()
            # self.click([(339,67), (490, 90)])
            # sleep(1)
            # self.driver.press_keycode(84)
            # sleep(4)
            self.click([(126, 322), (182, 350)])

            sleep(3)
            try:
                el1 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aq8")
                el1.click()
            except Exception as err:
                self.driver.back()
                continue

            num = 0
            sleep(3)
            while True:
                try:
                    if num >= 20:
                        self.driver.back()
                        self.driver.back()
                        break
                    try:
                        self.driver.swipe(start_x=self.x * 0.5, start_y=self.y * 0.88, end_x=self.x * 0.5,
                                          end_y=self.y * 0.35, duration=100)
                        num += 1
                    except Exception as err:
                        self.driver.back()
                        logging.error(err)
                except Exception as err:
                    self.driver.back()
                    logging.error(err)

    def get_fans_list(self):
        flag = True
        while flag:
            flag = self.click_home()
        sleep(5)
        for user in self.user.keys():
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
            sleep(2)
            while True:
                try:
                    el1 = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aq3")
                    el1.click()
                    break
                except Exception as err:
                    logging.error(err)
            sleep(2)
            num = 0
            while True:
                if num == 50:
                    num = 0
                    sql = f"""select count(*) from tiktok_fans_tests where user_id={self.user_id[user]}"""
                    '''
                    This is used to determine whether the number of fans has increased or not. If not, change the target.
                    用来判断粉丝是否还在增加，如果没有增加，则换一个粉丝。
                    '''
                    cc = self.get_mysql(sql)
                    print(cc)
                    if cc[0]['count(*)'] > 4900:
                        while True:
                            try:
                                self.driver.back()
                                break
                            except Exception as err:
                                pass
                        sleep(2)
                        while True:
                            try:
                                self.driver.back()
                                break
                            except Exception as err:
                                pass
                        break
                while True:
                    try:
                        self.driver.swipe(start_x=self.x * 0.5, start_y=self.y * 0.88, end_x=self.x * 0.5,
                                          end_y=self.y * 0.35)
                        num += 1
                        break
                    except Exception as err:
                        logging.error(err)

    def new_user(self):
        flag = True
        while flag:
            flag = self.click_home()
        sleep(5)

        for user in self.user.keys():

            try:
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
                print(user)
                num = 0
                next_cc = 0
                while True:

                    # sleep(random.uniform(0, 0.2))

                    if num == 20:
                        num = 0
                        sql = f"""select count(*) from tiktok_issue_test"""
                        '''
                        统计发布量，如果在如果数据没有增加，就换一个用户。
                        Statistics published, if in if the data does not increase, then another user.

                        '''
                        cc = self.get_mysql(sql)
                        print(cc, next_cc)

                        if cc[0]['count(*)'] == next_cc:
                            print("下一个")
                            break
                        else:
                            next_cc = cc[0]['count(*)']
                    else:
                        sleep(random.uniform(1, 2))
                        try:
                            self.driver.swipe(start_x=self.x * 0.5, start_y=self.y * 0.85, end_x=self.x * 0.5,
                                              end_y=self.y * 0.25)

                            num += 1
                        except Exception as a:
                            logging.error(a)
            except Exception as a:
                logging.error(f'{user, a}')
            self.driver.back()


def run_proxy(path):
    """
    用来开起对应的代理抓包
    :param path:
    :return:
    """
    os.system(fr'mitmdump -s {path} -p8888')


if __name__ == '__main__':
    pool = Pool(2)
    pool.apply_async(run_proxy, args=('proxy_file\\mitm_issue_user.py',))
    run = TikTok()
    run.new_user()
    pool.close()
    pool.join()
    # sleep(5)
    # run = TikTok()
    # run.get_fans_list()
    # pool = Pool(1)
    # pool.apply_async(run_proxy,args=('proxy_file\\mitm_comment.py',))
    # run = TikTok()
    # run.get_comment()
    # pool.close()
    # pool.join()
    # run = TikTok()
    # run.get_fans()
