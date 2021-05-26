class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.say(self.countAndSay(n-1))
    def say(self, s):
        s_list = list()
        i = int()
        j = int()
        while j <= len(s):
            if j == len(s):
                s_list.append(s[i:j])
                break
            elif s[j] == s[i] :
                j += 1
            else:
                s_list.append(s[i:j])
                i = j
        s = str()
        for i in s_list:
            s += str(len(i))
            s += i[0]

        return s
