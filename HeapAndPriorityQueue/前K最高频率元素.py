from collections import Counter
import heapq


class Solution(object):

    def top_k_frequent(self, A, k):
        counter = Counter(A)
        heap  = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == "__main__":

    s = Solution()
    res = s.top_k_frequent([1,2,3,3,4,4,5,5,5,3,3], 2)
    print(res)
