"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
Ref: https://leetcode.com/problems/factorial-trailing-zeroes/description/
"""


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else int(n/5) + self.trailingZeroes(int(n/5))

