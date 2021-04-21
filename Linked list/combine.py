# 合并两个有序链表

class ListNode(object):
    def __init(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def combine_ordered_link(self, head1, head2):
        dummy = ListNode()
        tail = dummy
        while head1 or head2:
            if head2 == None or head1 != None and head1.val < head2.val:
                tail.next = head1
                tail = head1
                head1 = head1.next
            else:
                tail.next = head2
                tail = head2
                head2 = head2.next

        tail.next = None

        return dummy.next