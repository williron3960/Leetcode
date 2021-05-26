class Solution:
    def __init__(self):
        self.stack = [[],[]]                       # stack[0] is the val ,stack [1] is the index
        self.result = [0,0]
        self.index = 1
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        # determine where invalid
        for i in range(len(s)):
            if s[i] == '(':
                self.stack[0].append('(')
                self.stack[1].append(i)
            else:
                if not self.stack[0] :
                    self.index += 1
                else:
                    self.stack[0].pop()
                    self.stack[1].pop()

        self.stack[0] = list()  # init the val
        self.index = 0


        for i in range(len(s)):
            if i in self.stack[1]:
                self.index += 1
                self.result.append(int())
            else:
                if s[i] == '(':
                    self.stack[0].append('(')
                else:
                    if not self.stack[0] :
                        self.index += 1
                        self.result.append(int())
                    else:
                        self.stack[0].pop()
                        self.result[self.index] += 2
        return max(self.result)
