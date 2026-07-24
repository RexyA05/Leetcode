class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        SortedNums=sorted(nums)
        rank={}
        for i,num in enumerate(SortedNums):
            if num not in rank:
                rank[num]=i
        return [rank[num] for num in nums]