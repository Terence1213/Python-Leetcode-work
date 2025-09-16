class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        repeated_chars = set() # This is for the case where we have more than a duplicate of a certain character, meaning that 
        # after removing it once from the hash_map, the next time it will be just added to the hash map normally as if its a unique character.

        for index, character in enumerate(s):
            if character in hash_map:
                # If we find a duplicate, we just remove that character, and so now we're ensuring that we have no duplicate characters.
                hash_map.pop(character)
                repeated_chars.add(character)
            elif character in repeated_chars: 
                pass
            else:
                hash_map[character] = index 
        
        if len(hash_map) == 0:
            return -1
        
        # Now all we have to do is return the character at the first index of hash_map.
        for character, index in hash_map.items():
            return index