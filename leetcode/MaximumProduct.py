#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
    which has the largest product.

    Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    Tag: DP
    https://leetcode.com/problems/maximum-product-subarray/
    """

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        local_max = []
        local_min = []

        max_product = None

        for num in nums:
            if max_product is None:
                local_max.append(num)
                local_min.append(num)
                max_product = num
            else:
                new_local_max = local_max[-1] * num
                new_local_min = local_min[-1] * num

                local_max.append(max(new_local_min, num, new_local_max))
                local_min.append(min(new_local_min, num, new_local_max))

                max_product = max(local_max[-1], max_product)

        return max_product


solution = Solution()
print(solution.maxProduct([-2, 0, -1]))
