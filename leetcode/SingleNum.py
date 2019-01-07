#!/usr/bin/python
# -*- coding: UTF-8 -*-

from functools import reduce


class Solution:
    """
    https://leetcode.com/problems/single-number
    给一个数组nums，其中只有一个数出现过一次，其余的全部都出现了两次，找出这个数
    """
    def single_num(self, nums):
        result = 0
        for num in nums:
            result = result ^ num

        return result

    def single_num2(self, nums):
        return reduce(lambda x, y:  x ^ y, nums)


# 测试
solution = Solution()
print(solution.single_num([1, 2, 3, 1, 2]))
print(solution.single_num2([1, 2, 3, 1, 2]))
