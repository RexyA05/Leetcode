from collections import deque

class Solution(object):
    def letterCasePermutation(self, S):
        result = deque([S])
        n = len(S)
        for i in range(n - 1, -1, -1):
            c = S[i]
            if c.isalpha():  # Fixed typo: isaplha -> isalpha
                size = len(result)
                while size > 0:
                    size -= 1  # Fixed logic bug: size=-1 -> size -= 1
                    s = result.popleft()
                    left = s[:i]
                    right = s[i+1:]
                    result.append(left + c.lower() + right)
                    result.append(left + c.upper() + right)
        return list(result)