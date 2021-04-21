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

#
# N = int(input())
# gift_money = list(map(int, input("").split()))
# M = int(input())
#
# res = mi_home_gift_bags(N, gift_money, M)
# if res:
#     print(1)
# else:
#     print(0)


# 集合覆盖
class Solution(object):

    def set_cover(self, states_needed, stations):
        final_station = set()

        while states_needed:
            best_station = None
            states_covered = set()
            for station, states_for_station in stations.items():
                covered = states_needed & states_for_station
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered
            states_needed -= states_covered
            final_station.add(best_station)
        return final_station

# if __name__=="__main__":
#     s = Solution()
#     s.set_cover(set([1,2,3,4]), {"a": set([1])})



