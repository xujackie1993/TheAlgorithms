class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):

    def reverse(self, head):
        dummy = ListNode()
        p = head

        while p:

            back = p.next
            p.next = dummy.next
            dummy.next = p
            p = back

    def reverseKGroup(self, head, k):
        ans = ListNode()
        ans_tail = ans

        tmp = ListNode()
        tmp_tail = tmp

        num = 0

        p = head

        while p:
            num += 1
            back = p.next
            p.next = None
            tmp_tail.next = p
            tmp_tail = p
            if num == k:
                ans_tail.next = self.reverse(tmp.next)
                ans_tail = tmp.next

                tmp.next = None
                tmp_tail = tmp
                num = 0


            p = back

        if num > 0:
            ans_tail.next = tmp.next

        return ans.next