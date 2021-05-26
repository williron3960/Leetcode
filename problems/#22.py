class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ['()']
        else:
            s_list = self.generateParenthesis(n-1)
            list_now = list()
            for i in range(len(s_list)):
                for j in range(len(s_list[i])):
                    list_now.append(s_list[i][:j] + '()' + s_list[i][j:])
            list_now = set(list_now)
            list_now = list(list_now)
            return list_now
