"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the ith position is divisible by i.
2. i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Note:
1. N is a positive integer and will not exceed 15.


Ref: https://leetcode.com/problems/beautiful-arrangement/description/
"""


class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        solves = []
        self.backtrack(solves, [], list(range(1, N+1)))
        return len(solves)

    # TimeLimit exceed
    def backtrack(self, solves, solve, remain):
        if not remain:
            solves.append(solve[:])
            return True
        idx = len(solve) + 1
        for i in range(len(remain)):
            if remain[i] % idx == 0 or idx % remain[i] == 0:
                solve.append(remain[i])
                self.backtrack(solves, solve, remain[0:i]+remain[i+1:])
                solve.pop()


print(Solution().countArrangement(15))