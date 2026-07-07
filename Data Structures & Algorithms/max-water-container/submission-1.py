class Solution:
    def maxArea(self, heights: List[int]) -> int:
        store = 0
        i = 0
        j = len(heights) -1
        length = j - i
        area = length *( min(heights[i], heights[j]) )
        while i < j:
            length = j - i
            area = length *( min(heights[i], heights[j]) )
            if (area > store):
                store = area
            if (heights[i] < heights[j]):
                i+=1
            else:
                j-=1
        return store

        
            