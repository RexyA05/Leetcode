class Solution(object):
    def twoSum(self, nums, target):
        indexed_nums = []
        for i in range(len(nums)):
            indexed_nums.append((nums[i], i))

        indexed_nums.sort()

        left = 0
        right = len(indexed_nums) - 1

        while left < right:
            total = indexed_nums[left][0] + indexed_nums[right][0]
            if total == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1

        return []