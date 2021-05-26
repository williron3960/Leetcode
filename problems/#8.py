class Solution:
    def __init__(self):
        self.sign = {'+','-'}
        self.result = str()
    def myAtoi(self, s: str) -> int:
        if not s.replace(' ',''):
            return 0
        s_list = list(s)
        while s_list[0] == ' ':
            del s_list[0]

        txt=str()                 # store the head element of s_list

        while s_list :
            txt=s_list.pop(0)
            self.result += txt
            if len (self.result) > 1 :
                if not  txt.isnumeric() :
                        break
            else:
                if not (txt.isnumeric() or txt in self.sign):
                    break

        if not self.result[-1].isnumeric():
            self.result = self.result[0:-1]

        if len(self.result) == 0 :
            return 0

        if (not self.result.isnumeric()) and len(self.result) == 1:
            return 0


        self.result = int(self.result)

        if self.result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif self.result < -1 * 2 ** 31:
            return -1 * 2 ** 31
        else:
            return self.result
