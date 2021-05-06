class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def findmiddle(self, head):
        s1 = head
        s2 = head
        pre = s1

        while s2 and s2.next:
            pre = s1
            s1 = s1.next
            s2 = s2.next.next
        return s1 if s2 else pre

    def split(self, head):
        mid = self.findmiddle(head)
        back = mid.next
        mid.next = None
        return mid, back