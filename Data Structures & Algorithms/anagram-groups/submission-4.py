"""
what do anagrams have in common, same frequency of characters

so create a tuple that states the frequncy of each character in the alphabet

then create a dict with that tuple as key and corresponding characters as values


creating the list
inspect each char in a string
list = [0]*26
for char in string:
    list[ord[char]-ord["a"]] = 1

dict[tuple(list)] = value
return list(dict.values()) becuase syntax error

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            l = [0]*26
            for char in string:
                l[ord(char)-ord("a")] += 1
            d[tuple(l)].append(string)
        return list(d.values()) 



        