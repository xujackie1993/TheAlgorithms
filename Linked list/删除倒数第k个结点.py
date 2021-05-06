class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeK(self, head, k):

        dummy = ListNode()
        dummy.next = head

        front = dummy
        preWalkedSteps = 0
        while (preWalkedSteps < k and front != None and front.next != None):
            front = front.next
            preWalkedSteps += 1

        back = dummy
        while (front != None and front.next != None):
            back = back.next
            front = front.next
        if preWalkedSteps == k:
            back.next = back.next.next

        return dummy.next
