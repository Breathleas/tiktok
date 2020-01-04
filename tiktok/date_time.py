# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 下午4:40
# @Author  : Wang Junling
# @File    : date_time.py
# @Software: PyCharm
import sxtwl
from datetime import datetime, timedelta


class ComputeDate(object):
    """
    实现输入一个时间点，计算出该时间点的起始点与结束点。
    """

    def __init__(self, date: str, N: int = 3):
        """
        初始化
        :param date:日期
        :param N: 单元区间值
        """
        self.N = N
        self.date = date
        self.date_year = int(date[:4])
        self.date_month = int(date[5:-2])
        self.date_day = int(date[-2:])

    def get_day(self, year: int = 0, month: int = 0, day: int = 0):
        """
        这样写的原因是希望之后可以复用此功能，直接调用．
        :param year: 年
        :param month: 月
        :param day: 日
        :return: 返回区间
        """
        if not year or not month or not day:
            year = self.date_year
            month = self.date_month
            day = self.date_day
        end = datetime(year, month, day)
        data = self.is_spring_day(year)

        if month < 2:
            year -= 1
        elif month == 2 and day < data[2]:
            year -= 1
        data = self.is_spring_day(year)
        start = datetime(data[0], data[1], data[2])

        da = end - start
        start_n = start + timedelta((da.days // self.N) * self.N)
        end_n = start + timedelta((1 + (da.days // self.N)) * self.N - 1)
        return str(start_n.date()).replace('-', ''), str(end_n.date()).replace('-', '')

    def is_spring_day(self, year: int):
        lunar = sxtwl.Lunar()
        for i in [3, 4, 5, 6, 7, 8]:
            day = lunar.getDayBySolar(year, 2, i)
            if day.jqmc:
                return year, 2, i


if __name__ == '__main__':
    run = ComputeDate('20180205', 3)
    print(run.get_day())
