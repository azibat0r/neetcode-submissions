"""
Flagging - Order can be different

So you want us to go through this list
look at each character
find another anagram
then group them together

anagram, same frequency of characters
O(m*n)



so essentially
we are building a dictionary
key = tuple representing the 26 letters in the alphabet
value = string in strs

so for the string act, its tuple would have 1 at the positions of a,c and t in the alphabet

the way to create said tuple
list = [0] * 26

list[ord(character) - ord("a")] += 1



steps
create result dictionary
key = tuple
value = list

check each string in strs
    create alphabet list for each strs
        check each char in strs
            at position of char in alphabet list add 1
    after making list add it to result dictionary and append to its value the string





"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            alph = [0] * 26
            for char in s:
                alph[ord(char)-ord("a")] +=1
            res[tuple(alph)].append(s)
        
        return list(res.values())


        