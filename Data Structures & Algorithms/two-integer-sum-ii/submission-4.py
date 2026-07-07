class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        ans = []
        total = 0
        while (len(ans) != 2):
            if ((numbers[left]+numbers[right]) == target):
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif ((numbers[left]+numbers[right]) > target):
                right-=1
            else:
                left+=1
