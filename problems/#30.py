class Solution:
    def findSubstring(self, s: str, words):

        self.lens_word = len(words[0])
        res = list()
        temp = words[:]
        self.lens = len(s) - self.lens_word * len(words)

        for i in range(self.lens + 1):
            words = temp[:]
            if self.match( s[ i : i + self.lens_word * len(words) ] , words ):
                res.append(i)
        return res

    def match(self, s, words):
        for i in range(len(s)//self.lens_word):
            temp = words
            if not ( s[ self.lens_word * i : self.lens_word * (i+1) ] in words):
                words = temp
                return False
            words.remove(s[ self.lens_word * i : self.lens_word * (i+1) ])
        words = temp
        return True
