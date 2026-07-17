class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen={}
        for index,num in enumerate(nums):
            if num in seen and index-seen[num]<=k:
                return True
            seen[num]=index
        return False

        
        