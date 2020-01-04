# Linux应用
 如何快速找出当前目录下最晚被修改过的文件？

- ls -lt

 已知某个进程的pid是6666,如何找到它当前打开了哪些文件？

-  lsof -p666

 发现端口8001被占用，如何找出是哪个进程占用了该端口？

- netstat -pan |grep 8001

 假设有进程P持续向文件F写入数据，此时把文件F删除，进程P的写入会失败吗？磁盘占用是否会持续增加？为什么？

- 不会失败，磁盘的占用还是会增加。因为程序还在使用该文件，只能等程序执行停止了，文件才会真正被删除。可以使用df来观察。

 给你一个文件，每行一个ip，如何用shell快速找到出现次数最多的ip？

- grep -Eo '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' ss.txt |sort | uniq -c|sort -r|head -n1

有如下分行的数据：

    |      32742 |
    |      39013 |
    |     481472 |
    |     481658 |
    |     481885 |
    
 把格式转换为：32742,39013,481337,481472,481658,481885
 写出你的办法
 shell 不太会，如果可以使用python很好解决，
    

# Python
为runner.py实现一个函数，检测是否有其他的runner.py进程在正在执行

    
            # -*- coding: utf-8 -*-
            # @Author  : Wang Junling
            # @Email   : wang_junling@yeah.net
            # @File    : a.py
            # @Software: PyCharm
            import os
            import psutil
            
            
            class Runner(object):
                """
                用来标明该类是用来干什么的__doc__
                """
            
                def get_pid(self):
                    """
                    获取当前运行模块的pid
                    :return: None
                    """
                    pid = os.getpid()
                    with open("process_id.log", 'w')as f:
                        f.write(str(pid))
            
                def is_read_pid(self):
                    """
                    用来查询该模块是否运行。
                    :return:
                    """
                    if os.path.exists("process_id.log"):
                        with open("process_id.log", 'r') as f:
                            pid = f.read()
                        return pid
                    else:
                        return False
            
                def run(self):
                    """
                    该程序的主函数
                    :return:
                    """
                    pid = int(self.is_read_pid())
                    if pid:
                        running_pid = psutil.pids()
                        if pid in running_pid:
                            print("process is running...")
                        else:
                            print('process no running...')
                    else:
                        self.get_pid()
                        print('process no running...')
            
            
            if __name__ == "__main__":
                main = Runner()
                main.run()


以每年的立春作为起始点，每N天为一个单元，任给一个日期，返回该日期所在单元的起始和结束日期。
例如：N=3, 输入日期20180208，返回 20180207,20180209（2018年的立春是20180204，
所以第一个单元是20180204-20180206，
第二个单元是 20180207-20180209，依次类推）
      编写一个类来实现以上功能。x
      
        # -*- coding: utf-8 -*-
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
