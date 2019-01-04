#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    Tag: DP
    https://leetcode.com/problems/maximum-subarray/
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        local = []
        max_sum = None

        for num in nums:
            if not local:
                local.append(num)
                max_sum = num
            else:
                local.append(max(local[-1] + num, num))
                max_sum = max(local[-1], max_sum)

        return max_sum
