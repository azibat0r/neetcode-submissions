"""
take in a list of string return string
take in str return list of string

what is important
turning the list into a string
then turning it back and

["12","32"]

so we do not add the delimiter inbetween because it can get confused with the string

we add the delimeter at the beginning


we use pointers
2#122#32

1 would be at 2
the other would identify the first #
then length would the window between the 2 pointers
and we can catch the actual string by using the window
given pointer i and j
string = [j+1:j+1+length]
then
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for char in strs:
            result += str(len(char)) + "#" + char
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []

        while j < len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            j = j+1+length
            i = j
        return result

