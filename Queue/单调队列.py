
class Queue(object):
    def __init__(self, cap):
        self.head = 0
        self.tail = 0
        self.cap = cap
        self.used = 0
        self.q = [0] * cap

    def backIndex(self):
        # 尾元素位置
        return (self.tail - 1 + self.cap) % self.cap


    def front(self):
        return self.a[self.head]


    def push(self, val):
        while self.used > 0 and self.q[self.backIndex()] < val:
            self.used -= 1
            self.tail = self.backIndex()
        self.q[self.tail] = val
        self.tail = (self.tail + 1) % self.cap
        self.used += 1

    def pop(self, val):
        if self.used > 0 and self.q[self.head] == val:
            self.used -= 1
            self.head = (self.head + 1) % self.cap

from collections import deque

class Solution(object):
    def maxSlidingWindows(self, nums, k):
        if not nums or len(nums) < k:
            return []
        Q = Queue(k)
        ans = []
        for i in range(0, len(nums)):
            Q.push(nums[i])
            if i < k - 1:
                continue
            ans.append(Q.front())
            Q.pop(nums[i-k+1])
        return ans


class Solution2(object):
    def __init__(self):
        self.Q = deque()

    def push(self, val):
        while self.Q and self.Q[-1] < val:
            self.Q.pop()
        self.Q.append(val)

    def pop(self, val):
        if self.Q and self.Q[0] == val:
            self.Q.popleft()

    def maxSilidingWindows(self, nums, k):
        if not nums or len(nums) < k:
            return []
        ans = []
        for i in range(0, len(nums)):
            self.push(nums[i])
            if i < k -1:
                continue
            ans.append(self.Q[0])
            self.pop(nums[k-i+1])
        return ans


