class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows>1:
            result=str()
            period=2*numRows-2
            for i in range(numRows):
                locals()['str'+str(i)]=str()
            for i in range(len(s)):
                loc=int(abs((i%period)-period/2))
                locals()['str'+str(loc)]=eval('str'+str(loc))+s[i]
            for i in range(numRows-1,-1,-1):
                result=result+eval('str'+str(i))
            return result
        else:
            return s
