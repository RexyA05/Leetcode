class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        ans=[1]*n
        prefix=[1]*n
        postfix=[1]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]        
        for i in range(n-2,-1,-1):
            postfix[i]=postfix[i+1]*nums[i+1]
        for i in range(n):
            ans[i]=prefix[i]*postfix[i]
        return ans
        