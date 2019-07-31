#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SingleListNode(object):
    """单节点类"""
    def __init__(self, _item, _next=None):
        self.item = _item
        self.next = _next


class SingleLinkedList(object):
    """单链表类"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, newdata):
        node = SingleListNode(newdata, _next=self.head)
        self.head = node

    def append(self, newdata):
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, newdata):
        """将newdata插入到pos之后"""
        if pos <= 0:
            self.add(newdata)
        else:
            node = SingleListNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, olddata):
        """从单链表中删除所有的olddata"""
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == olddata:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next

    def length(self):
        """返回单链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """打印整个单链表"""
        cur = self.head
        ls = []
        while cur is not None:
            ls.append(cur)
            cur = cur.next
        return ls

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur == data:
                return True
            else:
                cur = cur.next
        return False


class SingleCircleLinkedList(SingleLinkedList):
    """单向循环链表  继承单链表类"""
    def __init__(self):
        super(SingleLinkedList).__init__()

    def add(self, newdata):
        """将新节点添加到单向循环链表头部 即头指针指向新节点,尾节点的指针指向新节点,新节点的指针指向原头节点"""
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != cur:
                cur = cur.next
            cur.next = node
            node.next = self.head
            self.head = node

    def append(self, newdata):
        node = SingleListNode(newdata)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            cur = self.head
            while cur.next != cur:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def remove(self, olddata):
        cur = self.head
        pre = None
        if self.is_empty():
            return
        elif self.head.item == olddata:
            while cur.next != olddata:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            while cur.next != self.head:
                if cur.item == olddata:
                    pre.next = cur.next
                    return
                pre = cur
                cur = cur.next

    def length(self):
        if self.is_empty():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count


class DoubleLinkedNode(object):
    """双向链表节点类"""
    def __init__(self, _item, _prev=None, _next=None):
        self.item = _item
        self.prev = _prev
        self.next = _next


class DoubleLinkedList(SingleLinkedList):
    """双向链表类 继承自单链表类"""
    def __init__(self):
        super(SingleLinkedList).__init__()

    def add(self, newdata):
        node = DoubleLinkedNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, newdata):
        node = DoubleLinkedNode(newdata)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            node.prev = cur
            cur.next = node

    def insert(self, pos, newdata):
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = DoubleLinkedNode(newdata)
            cur = self.head
            count = 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            node.prev = cur
            cur.next.pre = node
            cur.next = node

    def remove(self, olddata):
        if self.is_empty():
            return
        elif self.head.item == olddata:
            if self.head.next is not None:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
        else:
            cur = self.head
            while cur.next is not None:
                if cur.item == olddata:
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                    return
                cur = cur.next


class DoubleCircleLinkedList(SingleCircleLinkedList):
    """双向循环链表"""
    def __init__(self):
        super(SingleCircleLinkedList).__init__()

    def add(self, newdata):
        node = DoubleLinkedNode(newdata)
        if self.is_empty():
            self.head = node
            node.prev = node
            node.next = node
        else:
            node.pre = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def append(self, newdata):
        node = DoubleLinkedNode(newdata)
        if self.is_empty():
            self.head = node
            node.prev = node
            node.next = node
        else:
            self.head.prev.next = node
            self.head.prev = node
            node.prev = self.head.prev
            node.next = self.head

    def insert(self, pos, newdata):
        if pos <= 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = DoubleLinkedNode(newdata)
            count = 0
            cur = self.head
            while count < pos - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            node.prev = cur
            cur.next = node
            cur.next.prev = node

    def remove(self, olddata):
        if self.is_empty():
            return
        elif self.head.item == olddata:
            if self.length() == 1:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.pre = self.head.prev
                self.head = self.head.next
        else:
            cur = self.head.next
            while cur != self.head:
                if cur.item == olddata:
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.nex
                cur = cur.next
        

















