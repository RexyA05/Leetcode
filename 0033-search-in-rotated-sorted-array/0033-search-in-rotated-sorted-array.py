class Solution(object):
    def search(self,nums, target):
        st = 0
        end = len(nums) - 1
        
        while st <= end:
            mid = st + (end - st) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[st] <= nums[mid]:
                if nums[st] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    st = mid + 1
                else:
                    end = mid - 1
        
        return -1
