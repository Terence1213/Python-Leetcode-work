class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        
        if n in memo:
            return memo[n] # This prevents us having to do any duplicate checks, especially for longer staircases.
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        memo[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return memo[n] 