#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        local = [1]
        longest = [1]

        for i in range(len(nums)):
            if not i:
                continue

            max_len = 1
            for j in range(i+1):
                if not j:
                    continue

                if nums[i] > nums[j-1]:
                    max_len = max(max_len, local[j-1] + 1)

            local.append(max_len)
            longest.append(max(longest[-1], local[-1]))

        return longest[len(nums)-1]
