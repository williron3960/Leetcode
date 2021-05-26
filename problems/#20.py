class Solution:
    def isValid(self, s: str) -> bool:
        data = {'{':'}','(':')','[':']'}
        stack = list()
        for i in s:
            if i in data:
                stack.append(i)
            elif not stack:
                return False
            elif i != data[stack[-1]]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True
