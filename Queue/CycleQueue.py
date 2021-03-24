# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
#
#
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。
# 但是使用循环队列，我们能使用这些空间去存储新的值。
#
# 你的实现应该支持如下操作：
#
#
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。


class MyCirculeQueue(object):

    def __init__(self, k):
        #  第一个元素所在位置
        self.front = 0
        # enQueue要存放的位置
        self.rear = 0
        self.used = 0
        self.a = [0] * k
        self.capacity = k

    def isEmpty(self):
        return self.used == 0

    def isFull(self):
        return self.used == self.capacity

    def enQueue(self, value):
        if self.isFull():
            return False
        self.a[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.used += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.a.pop()
        self.front = (self.front + 1) % self.capacity
        self.used -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.a[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        tail = (self.rear-1 + self.capacity) % self.capacity
        return self.a[tail]


class MyCircleQueue2(object):
    def __init__(self, k):
        self.front = 0
        self.rear = 0
        self.cap = k + 1
        self.a = [0] * (k+1)

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        nexRear = (self.rear + 1) % self.cap
        return nexRear == self.front

    def enQueue(self, value):
        if self.isFull():
            return False
        self.a[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.cap
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.a[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        tail = (self.rear - 1 + self.cap) % self.cap
        return self.a[tail]