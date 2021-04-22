# 给定K个有序列表
import heapq

class LinkNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def merge_k_list(self, arry):
        LinkNode.__lt__ = lambda x, y: x.val < y.val
        dummy = LinkNode()
        tail = dummy
        heap = [x for x in arry]
        heapq.heapify(heap)
        while heap:
            cur = heapq.heappop(heap)
            tail.next = cur
            tail = cur

            if cur.next:
                heapq.heappush(heap, cur.next)
        return dummy.next

    def merge_k_list2(self, arry):
        # 暴力法
        nodes = []
        head = point = LinkNode()
        for l in arry:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = LinkNode(x)
            point = point.next
        return head.next

    def merge_k_list3(self, arry):
        # 分治
        while len(arry) > 1:
            a = arry.pop() if len(arry) > 0 else None
            b = arry.pop() if len(arry) > 0 else None
            arry.insert(0, self.merge_two_lists(a, b))
        return None if len(arry) < 1 else arry[0]

    def merge_two_lists(self, l1, l2):
        dummy = LinkNode()
        tail = dummy
        while l1 or l2:
            if l2 == None or l1 != None and l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        tail.next = None
        return dummy.next


    

# lists = [[1,4,5],[1,3,4],[2,6]]
#
# heap = [x for x in lists]
# print(heap)
# heapq.heapify(heap)
# print(heap)
# cur = heapq.heappop(heap)
# print(cur)