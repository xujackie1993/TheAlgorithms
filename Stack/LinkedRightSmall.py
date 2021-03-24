# -*- coding=utf-8 -*-
# 找到数组中右边第一个比我小的元素


class Solution:

    def find_right_small(self, array):
        """
        使用递增栈
        :type array: list
        :rtype ans: list
        """
        if not array or len(array) == 0:
            return []
        # 给返回值赋值
        ans = [0] * len(array)

        # 栈   元素都是下标
        t = []
        # 遍历传入数组
        for i in range(0, len(array)):
            while len(t) > 0 and array[t[i-1]] > array[i]:
                # 当栈元素大于数组中元素时，记录该元素下标 值更大的要在栈中消失
                ans[t[i-1]] = i
                t.pop()
            # 剩下的入栈
            t.append(i)
        # 剩下在栈里的 因为没有元素能消除它们 将结果值为-1
        while len(t) > 0:
            ans[t[-1]] = -1
            t.pop()
        return ans

    def find_right_large(array):
        """
        使用递减栈
        :type array: list
        :rtype ans: list
        """
        if not array or len(array) == 0:
            return []
        ans = [0] * len(array)

        t = []

        for i in range(0, len(array)):
            while len(t) > 0 and array[t[-1]] < array[i]:
                ans[t[-1]] = i
                t.pop()
            t.append(i)
        while len(t) > 0:
            ans[t[-1]] = -1
            t.pop()
        return ans

    def find_left_small(array):
        """
        数组中左边第一个比我小的位置
        :type array: list
        :rtype ans: list
        """
        if not array or len(array) == 0:
            return []
        
        ans = [0] * len(array)

        t = []
        for i in range(len(array)-1, -1, -1):
            while len(t) > 0 and array[t[-1]] > array[i]:
                ans[t[-1]] = i
                t.pop()
            t.append(i)
        while len(t) > 0:
            ans[t[-1]] = -1
            t.pop()
        return ans
