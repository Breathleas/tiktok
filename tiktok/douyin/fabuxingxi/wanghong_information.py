# -*- coding: utf-8 -*-#
# Name:         wanghong_information
# Description:  
# Author:       Wang Junling
# Date:         2019/11/28

import os
import json
import openpyxl
# class Information(object):
#     def __init__(self):
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
#         self.name=''
openpyxl_data=[]
dict1={}
for root,folder_list,file_list in os.walk(r'D:\python\douyin\fabuxingxi\fabu_list'):
    # print(root,folder_list,file_list)
    for i in file_list:
        # print(i)
        with open(os.path.join(root,i),'r',encoding='utf-16') as f:
            data=f.readline()
            # print(data)
            dd=json.loads(data)
            dd=dd.get('aweme_list','')
            for li in dd:

                # print('发布ID',li.get('aweme_id'))
                # print('发布人ID',li.get('author_user_id'))
                # if li.get('author_user_id') not in dict1:
                #     dict1[li.get('author_user_id')] = 1
                # else:
                #     dict1[li.get('author_user_id')]=dict1[li.get('author_user_id')]+1
                d=li.get('statistics')
                openpyxl_data.append((li.get('author_user_id'),li.get('aweme_id'),d.get('comment_count'),d.get('digg_count'),d.get('download_count'),d.get('share_count')))
                #                       dd.get('nickname'),dd.get('signature'),dd.get('gender'),
                #                       dd.get('school_name'),dd.get('birthday'),dd.get('country'),dd.get('city'),
                #                       dd.get('total_favorited'),dd.get('mplatform_followers_count'),
                #                       dd.get('follower_count'),dd.get('following_count'),
                #                       dd.get('aweme_count'),dd.get('dongtai_count'),dd.get('favoriting_count'),
                #                       '暂时为空',dd.get('avatar_thumb').get('url_list')[0]))
                # print(dd)

# print(dict1)

output_file_name = 'fabu.xlsx'


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
    title_data = ('作者id', '视频id', '评论', '点赞', '下载', '转发')
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            ws.cell(row=i + 1, column=j + 1).value = target_list[i][j]

    # 保存表格
    wb.save(filename=output_file_name)


save_excel(openpyxl_data, output_file_name)


