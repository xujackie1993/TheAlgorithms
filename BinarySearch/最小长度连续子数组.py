class Solution:
    def minSubArrayLen(self, target, nums):
        if not nums or len(nums) < 2:
            return 0

        def getC(length, nums, target):
            sum = 0
            for i in range(0, len(nums)):
                sum += nums[i]
                if i < (length - 1):
                    continue
                if sum >= target:
                    return 0
                sum -= nums[i - (length - 1)]
            return -1

        left, right = 1, len(nums) + 1

        while left < right:

            mid = left + (right - left) // 2
            mov = getC(mid, nums, target)
            if mov < 0:
                left = mid + 1
            else:
                right = mid
        return left if len(nums) >= left else left

s = Solution()
res = s.minSubArrayLen(3, [5,2])
print(res)