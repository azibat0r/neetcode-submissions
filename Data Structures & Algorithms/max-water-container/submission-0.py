class Solution:
    def maxArea(self, heights: List[int]) -> int:
        store = 0
        i = 0
        j = 1
        for i in range(len(heights)):
            j = i+1
            while j < len(heights):
                length = j - i
                area = length *( min(heights[i], heights[j]) )
                if (area > store):
                    store = area
                    j+=1
                else: j+=1
        return store

            