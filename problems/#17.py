class Solution:
    def __init__(self):
        self.data={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                  '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                  '8':['t','u','v'],'9':['w','x','y','z']}
        self.lst=list()
        self.result=list()

    def letterCombinations(self, digits: str):
        # determine  whether it is empty
        if len(digits)==0:
            return list()

        index = [0,0,0,0]

        while index[0] < len(self.data[digits[0]]):
            temp = str()

            for i,n in enumerate(digits):
                temp += self.data[n][index[i]]

            self.result.append(temp)

            index[len(digits)-1] += 1

            for i in range(len(digits)-1,0,-1):
                if index[i] == len(self.data[digits[i]]):
                    index[i] = 0
                    index[i-1] += 1
        return self.result
