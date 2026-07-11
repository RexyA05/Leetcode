class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       comb=nums1+nums2
       comb.sort()
       n=len(comb)
       if n%2==0:
            return (comb[n//2-1]+comb[n//2])/2.0
       else:
            return float(comb[n//2])
        