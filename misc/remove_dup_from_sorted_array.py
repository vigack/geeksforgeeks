"""
Remove duplicate element from sorted array
Constraint: Remove inplace & O(1) extra space
Ref: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        type nums: List[int]
        rtype: int
        """
        idx1 = None
        idx2 = None
        for i in range(len(nums)-1):
            if idx1 is not None:
                if nums[i] == nums[idx1]:
                    idx2 = i
                else:
                    break
            elif nums[i] == nums[i+1]:
                idx1 = i
                break
        for j in range(idx1+1, ):
            nums[j] = None
        return

