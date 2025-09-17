from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first, we must take all of the strings and create a new list with each string being sorted.
        groups = {}

        for word in strs:
            key = ''.join(sorted(word)) # sorted(word) returns an array of characters, so we have to join a string with those characters so that we actually form a string.
        
            if key not in groups:
                groups[key] = []
        
            groups[key].append(word)
    
        return list(groups.values())