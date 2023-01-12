"""The issue is the bit limit causing the final answer in one case to show problems"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        quotient = 0
        divvy = 0
        neg = False

        if dividend < 0 and divisor<0:
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif dividend < 0:
            dividend = abs(dividend)
            neg = True
        elif divisor < 0:
            divisor = abs(divisor)
            neg = True


        if divisor ==1:
            if neg:
                return dividend - dividend - dividend

            return dividend
        

        if divisor> dividend:
            return 0


        for _ in range(dividend):

            if divvy>dividend:
                
                if neg:
                    q = quotient -1
                    return q-q-q
                else:
                    return quotient -1
            
            if divvy == dividend:
                if neg:
                    return quotient - quotient - quotient
                else:
                    return quotient

            divvy += divisor
            quotient += 1

        

s = Solution()

print(s.divide(-2147483647,-1))