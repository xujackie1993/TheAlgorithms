#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断能不能使用不同的产品（一个产品在礼包中最多出现一次）组合成一个金额
输入N
输入N个价格p 用单空格隔开
输入金额M

输出 能组合出来输出1 否则输出0
"""


def mi_home_gift_bags(n, set, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if set[n - 1] > sum:
        return mi_home_gift_bags(n-1, set, sum)
    else:
        return mi_home_gift_bags(n-1, set, sum-set[n-1]) or mi_home_gift_bags(n-1, set, sum)


N = int(input())
gift_money = list(map(int, input("").split()))
M = int(input())

res = mi_home_gift_bags(N, gift_money, M)
if res:
    print(1)
else:
    print(0)
