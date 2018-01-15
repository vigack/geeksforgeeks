"""
Roman integer decoder and encoder
Ref: https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and lookup[s[i]] < lookup[s[i+1]]:
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
        return res


