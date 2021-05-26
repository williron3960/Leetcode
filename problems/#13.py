class Solution:
    def __init__(self):
        self.data={'I':1,'V':5,'X':10,'L':50 ,'C':100,'D':500,'M':1000}
        self.lst=list()
    def romanToInt(self, s: str) -> int:
        self.lst=self.translate(s)
        self.lst.append(0)
        minus=[self.lst[i] for i in range(len(self.lst)-1) if self.lst[i+1]>self.lst[i]]
        res=sum(self.lst)-2*sum(minus)
        return res
    def translate(self,s):
        for i in range(len(s)):
            self.lst.append(self.data[s[i]])
        return self.lst
