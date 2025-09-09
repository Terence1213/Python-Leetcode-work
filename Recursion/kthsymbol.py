# Solution was too slow :(
class Solution:
    def kthGrammar(self, n: int, k: int=0) -> int:
        # Replace 0 with 01, and replace 1 with 10.
        return self.recursiveFunc(n, k, "0")

    def recursiveFunc(self, n, k, acc):
        if n == 1:
            result = [int(char) for char in acc]
            return result[k - 1] # considering that lists are naturally indexed by 0, and that we want to index by 1, then we have to decrement k by 1 so that 1 would refer to 0 technically.

        result_string = ""

        for num in str(acc):
            if num == '0':
                result_string += "01"
            elif num == '1':
                result_string += "10"
        
        return self.recursiveFunc(n - 1, k, result_string)

class Solution:
    def kthGrammar(self, n: int, k: int=0) -> int:
        if n == 1:
            return 0  # first row is always 0
                
        parent = self.kthGrammar(n - 1, (k + 1) // 2)  # find parent in previous row
        
        # If parent is 0 → children = [0, 1]
        # If parent is 1 → children = [1, 0]
        if k % 2 == 1:  # odd index → left child
            return parent
        else:           # even index → right child
            return 1 - parent