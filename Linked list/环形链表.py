class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def detect_cycle(self, head):
        if not head or not head.next:
            return None
        s1 = head
        s2 = head
        while s2 and s2.next:
            s1 = s1.next
            s2 = s2.next.next
            if s1 == s2:
                break
        if s1 != s2:
            return None

        s1 = head
        while s1 != s2:
            s1 = s1.next
            s2 = s2.next
        return s1
