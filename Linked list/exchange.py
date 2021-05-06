# 两两交换链表的节点

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def split(self, head):

        odd = ListNode()
        even = ListNode()

        odd_tail = odd
        even_tail = even

        p = head

        index = 1

        while p:
            back = p.next

            if index % 2 == 1:
                odd_tail.next = p
                odd_tail = odd_tail.next
            else:
                even_tail.next = p
                even_tail = even_tail.next

            p = back
            index += 1
        odd_tail.next = None
        even_tail.next = None
        return odd.next, even.next

    def merge(self, odd, even):

        isEven = True
        dummy = ListNode()
        tail = dummy


        while odd or even:
            if (not odd) or (isEven and even):
                tail.next = even
                even = even.next
            else:
                tail.next = odd
                odd = odd.next
            tail = tail.next
            isEven = not isEven
        tail.next = None

        return dummy.next

    def exchange(self, head):
        odd, even = self.split(head)
        return self.merge(odd, even)


