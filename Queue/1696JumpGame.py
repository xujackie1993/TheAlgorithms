"""
跳跃游戏
 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
#
# 一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1,
# i + k)] 包含 两个端点的任意位置。
#
# 你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。
#
# 请你返回你能得到的 最大得分 。

"""
from collections import deque


class Solution(object):

    def maxResult(self, nums, k):

        if not nums or k <= 0:
            return 0

        # 单调队列
        Q = deque()
        # 默认每一步的得分
        scores = [0] * len(nums)

        for i in range(0, len(nums)):
            if i - k > 0:
                if Q and Q[0] == nums[i-k-1]:
                    Q.popleft()

            scores[i] = (Q[0] + nums[i]) if Q else nums[i]

            while Q and Q[-1] < scores[i]:
                Q.pop()
            Q.append(scores[i])
        return scores[-1]



