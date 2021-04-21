# 移除链表元素
# 给定一个链表头及一个整数值，要求把链表里面等于整数值的结点都从链表中移除出去

class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution(object):

    def remove_element(self, head, val):
        dummy = ListNode()
        tail = dummy
        p = head
        while p:
            back = p.next
            if p.val != val:
                tail.next = p
                tail = p
            p = back
        tail.next = None
        return dummy.next



