class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in dictionary:  
                dictionary[key].append(word)
            else:
                dictionary[key] = []
                dictionary[key].append(word)

        finalList = []
        for i in dictionary.values():
            finalList.append(i)
        return finalList