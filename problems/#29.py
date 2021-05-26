class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        result = (abs(dividend) // abs(divisor)) * (dividend*divisor // (abs(dividend) * abs(divisor) )) 
        if result > 2 ** 31 -1:
            return 2 ** 31 -1
        elif result < -2 ** 31:
            return -2 ** 31
        return result
