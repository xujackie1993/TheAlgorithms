

# 设计一个链表
# 单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，
# next是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
# 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
#

# 单链表节点
class LinkedNode(object):
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None


# 单链表  包含伪头
# 假设链表中所有节点都是 0-index
class LinkedList(object):

    def __init__(self):
        self.head = LinkedNode(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = LinkedNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def delAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next


# 包含伪头 伪尾

class DoubleLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = LinkedNode(0)
        self.tail = LinkedNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        if index + 1 < self.size - index:
            cur = self.head
            for _ in range(index+1):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - index):
                cur = cur.next
        return cur.val

    def addAtHead(self, val):
        self.size += 1
        pred = self.head
        succ = self.head.next
        to_add = LinkedNode(val)
        to_add.prev = pred
        to_add.next = succ
        succ.prev = to_add

    def addAtTail(self, val):
        self.size += 1
        pred = self.tail
        succ = self.tail.prev
        to_add = LinkedNode(val)
        to_add.next = pred
        to_add.prev = succ
        succ.next = to_add
        pred.prev = to_add

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size += 1
        to_add = LinkedNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred








