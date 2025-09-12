class Solution:
    def get_next(self, n):
        total = 0
        while n > 0:
            digit = n % 10 # Gets the right digit.
            total += digit * digit
            n //= 10 # If we had 85, now we have 8, so whenever doing %10, we're going to get 8 instead of 5.
        
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()

        # we will keep looping until through the happy calculation we either get 1, or a value which we've already obtained and stored previously.
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        
        return n == 1 # true if n = 1, false if not.