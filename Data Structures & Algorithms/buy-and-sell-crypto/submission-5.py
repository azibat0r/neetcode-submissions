"""
10, 3 , 5, 6, 1, 7

smallest = 10
then 1
biggest = 5
4 > 6 -1
so biggest = 6

smallest 10 then 3 
3 - 5 = 2
3 - 6 = 3
3 - 1 = negative
so smallest = 1

so we find the first smallest
then we do subtraction witl all 
who ever has the biggest subtration that is what is returned

the smaller the better



"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        small = prices[0]
        result = 0
        for i in range(len(prices)):
            small = min(prices[i], small)
            result = max(result, prices[i]-small)
        return result


