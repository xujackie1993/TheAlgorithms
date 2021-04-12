from collections import Counter
import heapq


class Solution(object):

    def top_k_frequent(self, A, k):
        counter = Counter(A)
        heap  = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# 最高频率单次
    def top_k_frequent_word(self, A, k):
        if k <= 0 or len(A) < k:
            return []
        d_fre = {}
        for x in A:
            num = d_fre.get(x, 0)
            d_fre[x] = num + 1

        heap = []
        for k, v in d_fre.items():
            heapq.heappush(heap, (v, k))
            while len(heap) > k:
                heapq.heappush(heap)

        ans = []
        while len(heap) > 0:
            p = heapq.heappop(heap)
            ans.append(p[1])
        ans.reverse()
        return ans

    # 离原点最近的k个点
    def k_close(self, A, k):
        if k <= 0 or len(A) < k:
            return []


        def dist(t):
            x = t[0] * t[0]
            y = t[1] * t[1]
            return x + y

        heap = []
        for i in range(A):
            heapq.heappush(heap, (-dist(A[i]), k))
            while len(heap) > k:
                heapq.heappush(heap)

        ans = []
        while len(heap) > 0:
            p = heapq.heappop(heap)
            ans.append(p[1])
        return ans


if __name__ == "__main__":

    s = Solution()
    res = s.top_k_frequent([1,2,3,3,4,4,5,5,5,3,3], 2)
    print(res)
