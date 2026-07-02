class Solution(object):
    def romanToInt(self, s):
        map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        for i in range(len(s)):
            current_val=map[s[i]]
            if i+1<len(s):   
                next_val=map[s[i+1]]
                if current_val<next_val:
                    total-=current_val
                else:
                    total+=current_val
            else:
                total+=current_val
        return total


        
        