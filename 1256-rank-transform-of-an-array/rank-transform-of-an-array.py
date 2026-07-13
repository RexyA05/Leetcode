class Solution(object):
    def arrayRankTransform(self, arr):
        if len(arr) == 0:
            return []
        unique_sorted=sorted(set(arr))
        rankmap={}
        for index,values in enumerate(unique_sorted):
            rankmap[values]=index+1
        result=[]
        for num in arr:
            result.append(rankmap[num])
        return result

