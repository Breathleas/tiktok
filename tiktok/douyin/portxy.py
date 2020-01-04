# -*- coding: utf-8 -*-#
# Name:         portxy
# Description:  
# Author:       Wang Junling
# Date:         2019/12/11

import pymysql
import json
import re

connect = pymysql.connect(host='52.81.170.174',
                          user='wangjunling',
                          password='Wjl1314520.',
                          db='tiktok',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()
# 这个地方必须这么写 函数名：response
def response(flow):
    # print(flow.response.text)
    # 通过抓包软包软件获取请求的接口
    # print(flow)
    # if 'aweme/v1/user/follower/list' in flow.request.url:
    #     # 数据的解析
    #     for user in json.loads(flow.response.text)['followers']:
    #
    #         print(user)
    if '/aweme/v1/aweme/post/?' in flow.request.url:
        # 发布详细信息
        # print(flow.response.text)
        for user in json.loads(flow.response.text)['aweme_list']:
            # print(user)
            sql = f"""insert into tiktok.tiktok_issue_test(user_id,issue_id,json_content,date,type,flag) values (
                                {user.get('author_user_id')},{user.get('aweme_id')},
                                '{pymysql.escape_string(json.dumps(user, ensure_ascii=False))}',20191210,0,0)"""

            try:
                cursor.execute(sql)
                connect.commit()
            except Exception as err:
                print(err)
    # 用户详细信息插入
    if '/aweme/v1/user/?' in flow.request.url:
        if 'user_id = 962818056395822'not in flow.request.url:
            dd=json.loads(flow.response.text)['user']
            if int(dd.get('uid')) not in [55164137674]:
                # print(dd)
                sql = f"""insert into tiktok.tiktok_user_test(id,`user_id`,`json_content`,`date`,`type`,`flag`) values (
                      0,{dd.get('uid')},'{pymysql.escape_string(flow.response.text)}',20191210,0,0)"""
                try:
                    cursor.execute(sql)
                    connect.commit()
                except Exception as err:
                    print(err)
#
#     if '/aweme/v1/user/?sec_user_id=' in flow.request.url:
#         # print(flow.response.text)
#         data = flow.response.text
#
#
#         dd = json.loads(data)
#         #
#         dd = dd.get('user')
#         #             print('抖音ID', dd.get('uid'))
#         sql=f"""update  tiktok.tiktok_fans_test set json_content='{pymysql.escape_string(json.dumps(dd,ensure_ascii=False))}',tiktok.tiktok_fans_test.flag=0 where fans_user_id='{dd.get('uid')}'"""
#         try:
#
#             cursor.execute(sql)
#             connect.commit()
#         except Exception as err:
#             pass
# # uid=re.findall("sec_user_id=('')")
#
#     if 'aweme/v1/user/following/list/?user_id=' in flow.request.url:
#             uid = re.findall("\?user_id=(.*?)&sec_user_id",flow.request.url)
#             print(uid)
#             datas = json.loads(flow.response.text)['followings']
#             for data in datas:
#                 sql=f"""insert into tiktok.tiktok_fans_follower(user_id,kol_id,json_content,date,flag) values (
#                 {uid[0]},{data.get('uid')},'{pymysql.escape_string(json.dumps(data,ensure_ascii=False))}',20191211,0)"""
#                 # print(sql)
#                 try:
#
#                     cursor.execute(sql)
#                     connect.commit()
#                 except Exception as err:
#                     print(err)