class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        if len(needle) == 0 and len(haystack) == 0:
            return 0
        elif len(haystack) == 0:
            return -1

        # Brute force search -> We check each character one by one, if we find a character matching with the starting character of needle, we start checking whether there is a completely matching string
        # The way I'm planning to do this is that we append the characters to a list of characters for needle length amount of times, and then we compare strings.
        
        # In the case where we have ccar and we're searching for car, what are we going to do? we have c, so we're going to check cca, mark it as false, and then move on the r, which is bad.
        # Whenever we're performing a word check, we need to backtrack back on the index after the starting index of the word we were checking.

        result_indexes = [] # Contains the starting indexes at which we've found needle within haystack.
        index = 0

        while True:
            if haystack[index] == needle[0]:
                word = []
                for i in range(index, index + len(needle)): # So if the index is 0, and the length of the word is 3, then we're going to check through indexes 0 to 2, which makes sense
                    word.append(haystack[i])
                
                word_str = "".join(word)
                
                if word_str == needle:
                    result_indexes.append(index)
            
            index += 1

            # Lets say haystack is ilovedogs, and needle is luv. If we're past the character 'o' from haystack, then we can't form the whole word needle for sure so we stop.
            # length of iLovedogs: 9
            # Length of luv: 3
            # Index we have to stop at is 6 (so anything greater than 6 is bad). -> 9 - 3 = 6
            if index > len(haystack) - len(needle):
                break
        
        if len(result_indexes) == 0:
            return -1
        else:
            return result_indexes[0]

# More efficient solution
class SolutionTwo:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
    
        # using built in python algorithm for seeing whether the string exists.
        return haystack.find(needle)
