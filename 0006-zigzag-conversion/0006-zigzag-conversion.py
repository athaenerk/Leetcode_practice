class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 : return s
        o=""
        for r in range(numRows):
            #increment = 2*(numRows-1)
            for i in range(r,len(s),2*(numRows-1)):
                o+=s[i]
                if (r>0 and r<numRows-1 and i+2*(numRows-1)-2*r<len(s)):
                    o+=s[i+2*(numRows-1)-2*r]        
        return o