"""
[-1,0,1,2,-1,-4]

sort it

[-4,-1,-1,0,1,2]

first pointer on -4
l on -1
r on 2

add together you get -3 which is < 0
so make l+= 1
l on -1
+=1
0 you get -2
+=1
at 1 u get -1
and+=1
should break because l is not < r
after breaking we should make the
first pointer move to -1
and have the l pointer = the position ahead of first pointer
and r back to end of the list

i want the first pointer to increment until the 3rd to last of the list

"""

[-4,-1,-1,0,1,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        f = 0
        l = 1
        r = len(nums)-1

        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue
            while l < r:
                if nums[i]+nums[l]+nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l != r:
                        l+=1
                elif nums[i]+nums[l]+nums[r] > 0:
                    r-=1
                else:
                    l+=1
        return res
        