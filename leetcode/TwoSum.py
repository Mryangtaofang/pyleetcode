#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    https://leetcode.com/problems/two-sum/
    给一个数组nums，和一个目标数target，求两个数之和为target的下标
    """
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) <= 0:
            return

        my_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in my_map:
                return list((my_map[target - nums[i]], i))
            else:
                my_map[nums[i]] = i

        return

    def two_sum2(self, nums, target):
        """
        第二种写法
        """
        new_nums = nums[:]

        for num in nums:
            new_nums.remove(num)
            if (target - num) in new_nums:
                if target - num == num:
                    return [i for i, x in enumerate(nums) if x == num]
                else:
                    return sorted([nums.index(num), nums.index(target - num)])
            new_nums = nums[:]


# 测试
solution = Solution()
result1 = solution.two_sum([1, 2, 3, 4], 7)
result2 = solution.two_sum2([1, 2, 3, 4], 7)
print(result1, result2)
