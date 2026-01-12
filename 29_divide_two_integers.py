class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
            
        negative = (dividend < 0) != (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ans = 0

        while dividend >= divisor:
            temp = divisor
            count = 1
            
            while dividend >= (temp<< 1):
                temp<<= 1
                count <<= 1
            
            dividend -= temp
            ans += count

        return -ans if negative else ans
