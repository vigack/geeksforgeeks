"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

Ref: https://leetcode.com/problems/excel-sheet-column-title/description/
"""

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

