"""
当 while (left < right) 时，对应的更新式是 left = middle + 1 ， right = middle

当 while (left <= right) 时，对应的更新式是 left = middle + 1，right = middle - 1
"""


class Solution(object):

    def binary_search(self, A, target):
        left = 0
        right = len(A) if A else 0
        if not A:
            return -1
        while left < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid
        return -1

    def search_range(self, nums, target):
        """排序列表中查找元素的第一个和最后一个元素"""
        if not nums or len(nums) == 0:
            return [-1, -1]

        def lower_index(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_index(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = lower_index(nums, target)
        end = upper_index(nums, target)
        if start == end:
            return [-1, -1]
        return [start, end-1]


if __name__ == "__main__":
    s = Solution()
    s.search_range([1,1,3,4], 2)







