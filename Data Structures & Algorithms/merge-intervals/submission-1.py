"""
correct check
but think of 

1,4  2,5  3,6
you merge
and get
1,5 this output should also be used to check 3,6
and final output is 1,6



so you put the first interval in output

then compare the first of subsequent intervals with its last
if first <= last, then we update the output last to be the max of the two intevals

and if it fails
we append the current interval and the check with that interval from then on
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        output = []
        output.append(intervals[0])
        for a,b in intervals:
            if a <= output[-1][1]:
                output[-1][1] = max(b,output[-1][1])
            else:
                output.append([a,b])
        return output

        