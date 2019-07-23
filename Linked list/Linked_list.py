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
