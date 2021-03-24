# 滑动窗口最大值


# 使用循环队列 实现单调队列
class Queue(object):
    def __init__(self, k):
        self.cap = k
        # 第一个元素的位置
        self.front = 0
        # 将要存放的位置
        self.rear = 0
        self.used = 0
        self.q = [0] * k

    def tailIndex(self):
        # 队列尾元素索引
        return (self.rear - 1 + self.cap) % self.cap

    def push(self, val):
        while self.used > 0 and self.q[self.tailIndex()] < val:
            self.rear = self.tailIndex()
            self.used -= 1
        self.q[self.rear] = val
        self.rear = (self.rear + 1) % self.cap
        self.used += 1

    def pop(self, val):
        if self.used > 0 and self.q[self.front] == val:
            self.front = (self.front + 1) % self.front
            self.used -= 1

    def Front(self):
        return self.q[self.front]



class Solution(object):

    def maxSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []

        Q = Queue(k + 1)

        ans = []
        for i in range(0, len(nums)):
            Q.push(i)
            if i < k - 1:
                continue

            ans.append(Q.Front())
            Q.pop(i-k+1)
        return ans


from collections import deque


class Solution2(object):
    def __init__(self):
        self.Q = deque()

    def push(self, v):
        while self.Q and self.Q[-1] < v:
            self.Q.pop()
        # 将元素入队
        self.Q.append(v)

    def pop(self, v):
        if self.Q and self.Q[0] == v:
            self.Q.popleft()

    def max_sliding_window(self, nums, k):
        if not nums or len(nums) < k:
            return []
        ans = []
        for i in range(0, len(nums)):
            self.Q.append(nums[i])
            if i < k - 1:
                continue
            ans.append(self.Q[0])
            self.Q.pop(nums[i-k+1])
        return ans
