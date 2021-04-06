
"""
堆
"""
class Heap(object):
    a = []
    n = 0

    # 上浮
    def _swim(self, i):
        t = self.a[i]
        while i > 0:
            par = (i - 1) / 2       # 父节点
            if self.a[par] < t:
                self.a[i] = self.a[par]
                i = par
            else:
                break
        self.a[i] = t

    # 下沉
    def _sink(self, i):
        t = self.a[i]
        while i + i + 1 < self.n:
            j = i + i + 1             # 子节点
            if j < self.n - 1 and self.a[j] < self.a[j+1]:
                j += 1
            if self.a[j] > t:
                self.a[i] = self.a[j]
                i = j
            else:
                break
        self.a[i] = t


    # 往堆尾添加新的元素  新来元素 a[n]上浮
    def push(self, v):
        self.a.append(v)
        self._swim(self.n)
        self.n += 1


    # 移除堆首 将最后一个元素移到第一位 然后下沉
    def pop(self):
        ret = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.a.pop()
        self.n -= 1
        self._sink(0)
        return ret

    def size(self):
        return self.n

