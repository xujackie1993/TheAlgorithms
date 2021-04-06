"""
最小的k个数
给定数组a[],返回数组中最小的K个数
"""
class Heap(object):
    def __init__(self):
        self.a = []
        self.n = 0

    # 上浮
    def swim(self, i):
        t = self.a[i]

        while i > 0:
            j = (i - 1) / 2  # 父节点
            if self.a[j] < self.a[i]:
                self.a[j] = self.a[i]
                i = j
            else:
                break
        self.a[i] = t


    # 下沉
    def sink(self, i):
        t = self.a[i]
        while i + i + 1 < self.n:
            j = i + i + 1  # 子节点
            if self.a[j] < self.a[j + 1]:
                j += 1
            if self.a[j] > t:
                self.a[i] = self.a[j]
                i = j
            else:
                break
        self.a[i] = t

    def push(self, v):
        self.a.append(v)
        self.swim(self.n)
        self.n += 1



    # 移除堆首
    def pop(self):
        self.a[0] = self.a[self.n-1]
        self.a.pop()
        self.n -= 1
        self.sink(0)

    def size(self):
        return self.n


def smallest_k_number(arry, k):
    if k <= 0 or not arry or len(arry) < k:
        return -1

    heap = Heap()

    for r in range(len(arry)):
        heap.push(arry[r])
        while heap.size() > k:
            heap.pop()
    return heap.a



# 使用内置的堆

from queue import PriorityQueue

class Solution(object):

    def getleastNumbers(self, arry, k):
        if k <= 0 or not arry or len(arry) < k:
            return -1
        Q = PriorityQueue()
        for x in arry:
            Q.put(x)
            while Q.qsize() > k:
                Q.get()
        ans = []
        while not Q.empty():
            ans.append(Q.get())
        return ans
