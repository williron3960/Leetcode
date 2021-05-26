class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if not needle in haystack:
            return -1
        else:
            return haystack.find(needle,0)
