# -*- coding=utf-8 -*-
# 柱状图中最大矩形

class Solution:

    def largestRectangleArea(self, heights):
        """
        :type heights: list
        :rtype max: int
        """
        if not heights or len(heights) == 0:
            return 0
        left_ans = [0] * len(heights)
        right_ans = [0] * len(heights)
        stack = []
        for i in range(0, len(heights)):
            while len(stack) > 0 and stack[-1] > heights[i]:
                right_ans[stack[-1]] = i
                stack.pop()
            stack.append(i)
        while len(stack) > 0:
            right_ans[stack[-1]] = -1
            stack.pop()
        
        stack = []
        for j in range(len(heights)-1, -1, -1):
            while len(stack) > 0 and stack[-1] > heights[i]:
                stack.pop()
            left_ans[j] = stack[-1] if stack else -1
            stack.append(j)

        ans = 0
        for i in range(0, len(heights)):
            height = heights[i]
            rightPos = right_ans[i] if right_ans[i] != -1 else len(heights)
            leftPos =  left_ans[i]
            ans = max(ans, height * (rightPos - leftPos - 1))
        return ans