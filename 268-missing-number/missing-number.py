class Solution(object):
    def missingNumber(self, nums):
        high=len(nums)
        for i in range(high+1):
            if i not in nums:
                return i


        