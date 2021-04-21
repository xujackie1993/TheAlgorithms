"""
反转链表
"""
class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    # 头部插入
    def reverse_list(self, head):
        dummy = LinkedNode(0)
        p = head
        while p:
            back = p.next

            p.next = dummy.next
            dummy.next = p

            p = back
        return dummy.next


