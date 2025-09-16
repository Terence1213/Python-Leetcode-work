# My solution (too slow)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.pow(x, n, 1)
    
    def pow(self, x, n, result) -> float:
        if n == 0:
            return result
        
        if n < 0:
            return self.pow(1/x, -n, result)
        
        return self.pow(x, n - 1, result * x)

# Chat gpt solution
class SolutionTwo:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n < 0:
            x, n = 1 / x, -n
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result