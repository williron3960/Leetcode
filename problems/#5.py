class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > self.maximum_length:
                    self.start = left
                    self.end = right
                    self.maximum_length = right - left + 1
                left -= 1
                right += 1
        # Update the following variables every time a palindromic
        # string of greater length is discovered
        self.maximum_length = 0
        self.start = 0
        self.end = 0
        # Expand for each i.
        for i in range(1, len(s)):
            expand(i-1, i+1) # For odd length strings like abbba
            expand(i-1, i) # For even length strings like abba
        return s[self.start:self.end+1]
