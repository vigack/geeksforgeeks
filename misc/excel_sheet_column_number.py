"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Ref: https://leetcode.com/problems/excel-sheet-column-number/description/
"""

from functools import reduce


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda n,ch:n*26+ord(ch)-64, s, 0)


print(Solution().titleToNumber("AB"))

