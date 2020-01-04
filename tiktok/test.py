# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 下午4:49
# @Author  : Wang Junling
# @File    : test.py
# @Software: PyCharm
foo = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54}, {"name": "wa", "age": 17}, {"name": "df", "age": 23}]
print(sorted(foo, key=lambda x: x['age']))

'''
给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：

每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

示例 1：

输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。
示例 2：

输入：nums = [9,6,1,6,2]
输出：4

'''
import numpy as np
import random


def funCear(nums: list):
    len_nums = len(nums)
    list1 = [0]
    list2 = [0]
    flag = 0

    for i in range(len_nums - 1):
        if i % 2 == flag:
            print(nums[i], nums[i + 1])
            print(nums[i] > nums[i + 1])
            if nums[i] > nums[i - 1]:
                list1.append(abs(nums[i] - nums[i - 1]) + 1)
            if nums[i] < nums[i + 1]:
                list2.append(abs(nums[i] - nums[i + 1]) + 1)
        else:
            print(nums[i], nums[i + 1])
            print(nums[i] < nums[i + 1])
            if nums[i] < nums[i + 1]:
                list1.append(abs(nums[i] - nums[i + 1]) + 1)
            if nums[i] > nums[i + 1]:
                list2.append(abs(nums[i] - nums[i + 1]) + 1)

    print(list1)
    print(list2)
    if max(list1)>max(list2):
        print(max(list2))
    else:
        print(max(list1))


if __name__ == '__main__':
    a = [7,4,8,9,7,7,5]
    #    0  1  0  1  0  1

    funCear(a)
