class Solution:
    def fib(self, n: int, memo={}) -> int:
        # We start with the largest number, and stop until the first number which we know to be 0.
        if n in memo:
            return memo[n]
        
        if n == 0: 
            return 0
        if n == 1:
            return 1
        
        memo[n] = self.fib(n - 2, memo) + self.fib(n - 1, memo)
        return memo[n]