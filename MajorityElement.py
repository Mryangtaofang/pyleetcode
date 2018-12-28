#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    多数投票法
    https://leetcode.com/problems/majority-element
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        result = 0
        for num in nums:
            if total == 0:
                result = num
            total += (1 if num == result else -1)

        return result


solution = Solution()
print(solution.majorityElement([2, 3, 3, 3]))
