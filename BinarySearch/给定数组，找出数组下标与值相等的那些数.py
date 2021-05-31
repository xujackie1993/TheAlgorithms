
class Solution(object):

    def getNumberSameIndex(self, nums):
        if not nums or len(nums) == 0:
            return -1

        def getC(i):
            v = nums[i]
            if v < i:
                return -1
            elif v == i:
                return 0
            else:
                return 1

        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            mov = getC(mid)
            if mov < 0:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == left:
            return left
        return -1


    def getMinSubArry(self, nums, target):
        """最小长度连续子数组"""
        if not nums or len(nums) == 0:
            return 0

        def getC(len):
            sum = 0
            for i in range(0, len(nums)):
                sum += nums[i]
                if i < (len-1):
                    continue
                if sum >= target:
                    return 0
                sum -= nums[i-(len-1)]
            return -1

        left, right = 1, len(nums) + 1
        while left < right:
            mid = left + (right-left) // 2
            mov = getC(mid)
            if mov < 0:
                left = mid + 1
            else:
                right = mid
        return left if left <= len(nums) else 0
