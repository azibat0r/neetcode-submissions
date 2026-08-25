class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def repeat(path, nums, i):

            #basecase?
            if i > len(nums)-1:
                result.append(path[:])
                return

            path.append(nums[i])
            repeat(path, nums, i+1) #fall into including everything but now path is full
            
            path.pop()
            repeat(path,nums, i+1)
            #i want to delete of paths content make it dissapear

        repeat(path, nums, 0)
        return result
