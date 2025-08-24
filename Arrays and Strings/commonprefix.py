from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We have to compare the list of strings' first characters, and see if they match, we start with the first character, if it matches, we move on, if it doesn't then there is not prefix at all.
        # To determine how many times we're going to keep looping (as a maximum amount of loops), we must find the smallest string out of all of the strings.

        shortest_length = 10000 # Assuming that we're never going to have a string with a length greater than 10000
        for word in strs:
            if len(word) < shortest_length:
                shortest_length = len(word)
        
        prefix = []

        # The maximum amount of times we will loop depends on the shortest length
        for i in range(0, shortest_length):
            # We need to get the i index of each string, to do this with each string, we can perform a for loop.
            characters = [] 
            for word in strs:
                characters.append(word[i])
            
            if len(set(characters)) == 1: # Turning the list into a set removes any duplicate values, so if they were all 'a', or all the same character, the length will be one.
                prefix.append(characters[0])
            else:
                break

        return "".join(prefix)
            
        
