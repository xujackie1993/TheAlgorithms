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


# lists = [[1,4,5],[1,3,4],[2,6]]
#
# heap = [x for x in lists]
# print(heap)
# heapq.heapify(heap)
# print(heap)
# cur = heapq.heappop(heap)
# print(cur)