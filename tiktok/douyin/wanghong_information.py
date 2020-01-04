# -*- coding: utf-8 -*-#
# Name:         wanghong_information
# Description:  
# Author:       Wang Junling
# Date:         2019/11/28

import os
import json
import openpyxl
import pymysql

connect = pymysql.connect(host='52.81.170.174',
                          user='wangjunling',
                          password='Wjl1314520.',
                          db='tiktok',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()
import time

sql = """select * from tiktok_fans_tests where user_id in (68354827719,2334997990873038,3003501057414974)"""
cursor.execute(sql)

datas = cursor.fetchall()
openpyxl_data = []
dict1 = {}
for data in datas:
    print(data)

    data_json = json.loads(data.get('json_content'))
    # timeArray = time.localtime(int(data_json.get('create_time')))
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    otherStyleTime=data.get('date')
    tongji = data_json.get('statistics')
    openpyxl_data.append((data.get('user_id'), data.get('issue_id'), otherStyleTime,
                          tongji.get('digg_count'),tongji.get('share_count'),tongji.get('comment_count')))

output_file_name = 'xingd.xlsx'


def save_excel(target_list, output_file_name):
    """
    将数据写入xlsx文件
    """
    if not output_file_name.endswith('.xlsx'):
        output_file_name += '.xlsx'

    # 创建一个workbook对象，而且会在workbook中至少创建一个表worksheet
    wb = openpyxl.Workbook()
    # 获取当前活跃的worksheet,默认就是第一个worksheet
    ws = wb.active
    title_data = ('粉丝ID', '粉丝年龄', '粉丝性别')
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            ws.cell(row=i + 1, column=j + 1).value = target_list[i][j]

    # 保存表格
    wb.save(filename=output_file_name)


save_excel(openpyxl_data, output_file_name)
