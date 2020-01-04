# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 13:29
# @Author  : Wang Junling
# @Email   : wang_junling@yeah.net
# @File    : lingshi.py
# @Software: PyCharm
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

sql="""select * from tiktok_issue_test"""
cursor.execute(sql)

datas=cursor.fetchall()
openpyxl_data=[]
dict1={}
for data in datas:
    print(data)

    data_json=json.loads(data.get('json_content'))
    timeArray = time.localtime(int(data_json.get('create_time')))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    openpyxl_data.append((data.get('user_id'),data.get('issue_id'),otherStyleTime,data_json.get('share_url')))


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
    title_data = ('作者id', '视频id', '日期', '转发')
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            ws.cell(row=i + 1, column=j + 1).value = target_list[i][j]

    # 保存表格
    wb.save(filename=output_file_name)


save_excel(openpyxl_data, output_file_name)
