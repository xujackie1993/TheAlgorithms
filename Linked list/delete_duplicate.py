# 给定按升序排列的链表，删除重复元素
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    def delete_duplicate(self, head):
        # dummy = ListNode(0)
        # tail = dummy
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
        # while p:
        #     back = p.next
        #     if tail == dummy:
        #         tail
        #
        #     p = back

