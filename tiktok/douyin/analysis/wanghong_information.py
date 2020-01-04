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
for root,folder_list,file_list in os.walk(r'D:\python\douyin\analysis\user'):
    # print(root,folder_list,file_list)
    for i in file_list:
        with open(os.path.join(root,i),'r',encoding='utf-16') as f:
            data=f.readline()
            # print(data)
            dd=json.loads(data)





            dd=dd.get('user')
            print('抖音ID',dd.get('uid'))
            print('抖音名',dd.get('nickname'))
            print('简介',dd.get('signature'))
            print('性别', dd.get('gender'))
            print('学校', dd.get('school_name'))

            print('出生日',dd.get('birthday'))
            print('地区',dd.get('country'))
            print('城市',dd.get('city'))

            print('点赞',dd.get('total_favorited'))
            print('抖音+头条+火山',dd.get('mplatform_followers_count'))
            print('抖音粉丝',dd.get('follower_count'))
            print('关注',dd.get('following_count'))
            print('发布',dd.get('aweme_count'))
            print('动态',dd.get('dongtai_count'))
            print('喜欢',dd.get('favoriting_count'))
            print('头像url',dd.get('avatar_thumb').get('url_list'))
            openpyxl_data.append((dd.get('uid'),
                                  dd.get('nickname'),dd.get('signature'),dd.get('gender'),
                                  dd.get('school_name'),dd.get('birthday'),dd.get('country'),dd.get('city'),
                                  dd.get('total_favorited'),dd.get('mplatform_followers_count'),
                                  dd.get('follower_count'),dd.get('following_count'),
                                  dd.get('aweme_count'),dd.get('dongtai_count'),dd.get('favoriting_count'),
                                  '暂时为空',dd.get('avatar_thumb').get('url_list')[0]))
            # print(dd)



output_file_name = 'basic_information.xlsx'


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
    title_data = ('抖音ID', '抖音名', '简介', '性别', '学校', '出生日', '地区', '城市', '点赞', '抖音+头条+火山粉丝', '抖音粉丝', '关注', '发布','动态','喜欢','转发','头像url')
    target_list.insert(0, title_data)
    rows = len(target_list)
    lines = len(target_list[0])
    for i in range(rows):
        for j in range(lines):
            ws.cell(row=i + 1, column=j + 1).value = target_list[i][j]

    # 保存表格
    wb.save(filename=output_file_name)


save_excel(openpyxl_data, output_file_name)


