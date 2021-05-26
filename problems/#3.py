class Solution:
    def __init__(self):
        self.result = int()
        self.temp_list  = [[]]
        self.temp_list_index=[[]]
        self.temp_index = 0                       #define the i-th non-repeating characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>0:
            i = 0
            while i < len(s):
                if s[i] in self.temp_list[self.temp_index]:
                    index = self.temp_list[self.temp_index].index(s[i])
                    index = self.temp_list_index[self.temp_index][index]
                    self.temp_index += 1
                    self.temp_list.append([])
                    self.temp_list_index.append([])
                    i = index+1
                else:
                    self.temp_list[self.temp_index].append(s[i])
                    self.temp_list_index[self.temp_index].append(i)
                    i += 1

            for i in self.temp_list:
                if len(i) > self.result :
                    self.result = len(i)
            return self.result
        else:
            return 0
