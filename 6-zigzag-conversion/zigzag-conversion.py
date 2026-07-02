class Solution(object):
    def convert(self, s, numRows):
        if numRows==1 or numRows>=len(s):
            return s
        rows=[""]*numRows
        currentRow=0
        direction=-1
        for ch in range(len(s)):
            rows[currentRow]+=s[ch]
            if currentRow==0 or currentRow==numRows-1:
                direction=-direction
            currentRow+=direction
        return "".join(rows)
        