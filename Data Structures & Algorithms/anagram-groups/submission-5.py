"""
an anagram ia 2 characters that have the same number of characters appearing with the same frequency

create a list represnting all characters in the alphabet
[0]*26
find the position for each character in the string in the alphabet
ord("a")-ord("character") += 1

use that list which u would turn to a tuple as the key to a dictionary

and return its values
list(hashmap.values())



"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for char in strs:
            alphabet = [0]*26
            for c in char:
                alphabet[ord(c)-ord("a")] += 1
            hashmap[tuple(alphabet)].append(char)
        return (list(hashmap.values()))
        



        