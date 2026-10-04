"""
prices = [10,1,5,6,7,1]

so we are looking for the smallest to buy
and biggest to sell

so walking through it
10 is buy
then we look at 1
10 > 1
so 1 becomes buy
then we look at
since 1 < 5
we calculate difference
and save it to maximum
and so on

so our buy would always be the first element in the list
and we iterate we check if the current is smaller than our buy

for i in range(len(prices)):
    if i is < than buy
        buy = i
        continue
    difference = i - buy

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                continue
            dif = prices[i] - buy
            answer = max(dif,answer)
        return answer

        