class Solution:
    def __init__(self):
        self.result=str()
        self.list=list()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>0:
            mini=1000000
            for i in range(len(strs)):
                if mini>len(strs[i]):
                    mini=len(strs[i])
            i=0
            while i<mini:
                self.list.append(strs[0][i])
                for j in range(1,len(strs)):
                    if strs[j][i]!=self.list[i]:
                        return self.result
                self.result=self.result+self.list[-1]
                i+=1
            return self.result
        else:
            return ''
