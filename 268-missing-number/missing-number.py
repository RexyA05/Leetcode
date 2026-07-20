class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        summation=0
        actual_sum=(n*(n+1))/2
        for i in range(n):
            summation+=nums[i]
        missing_num=(actual_sum-summation)
        return missing_num



        