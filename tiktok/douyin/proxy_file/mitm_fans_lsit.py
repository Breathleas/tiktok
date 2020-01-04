# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 13:39
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : mitm_fans_lsit.py
# @Software: PyCharm
import pymysql
import json
import logging
import time
import re
# 这个地方必须这么写 函数名：response
LOGGING_FORMAT = '%(asctime)-15s:%(levelname)s: %(message)s'
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO,
                    filename='mitmprotxy.log', filemode='a', )
connect = pymysql.connect(host='52.81.170.174',
                          user='wangjunling',
                          password='Wjl1314520.',
                          db='tiktok',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()

def response(flow):
    # 通过抓包软包软件获取请求的接口
    if 'aweme/v1/user/follower/list/?' in flow.request.url:
        # 发布详细信息
        uid=re.findall("\?user_id=(.*?)&sec_user_id", flow.request.url)[0]
        for fans in json.loads(flow.response.text)['followers']:
            # print(fans)
            sql = f"""insert into tiktok.tiktok_fans_tests(user_id,fans_user_id,short_id,unique_id,json_content,date,flag)
             values ({uid},{fans.get('uid')},'{fans.get('short_id')}','{fans.get('unique_id')}',
                                '{pymysql.escape_string(json.dumps(fans, ensure_ascii=False))}',
                                {time.strftime("%Y%m%d", time.localtime())},0)"""
            '''
            粉丝数据入库。截获粉丝数据包，分析出其中的uid，和搜索id，爬虫时间，和json格式。
            
            '''
            try:
                cursor.execute(sql)
                connect.commit()
            except Exception as err:
                logging.error(err)
