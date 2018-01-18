"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Ref: https://leetcode.com/problems/permutations/description/
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solves = []
        self.backtrack(solves, [], nums)
        return solves

    def backtrack(self, solves, solve, remain):
        if not remain:
            solves.append(solve[:])
        for num in remain:
            solve.append(num)
            self.backtrack(solves, solve, [x for x in remain if x!=num])
            solve.pop()


print(Solution().permute([1,2,3]))