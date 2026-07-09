class Solution(object):
    def isValid(self, s):
        stk=[]
        dict={')':'(',']':'[','}':'{'}
        for char in s:
            if char in dict:
                if not stk or stk[-1]!=dict[char]:
                    return False
                else:
                    stk.pop()
            else:
                stk.append(char)
        return not stk

