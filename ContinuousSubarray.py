#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    给定一个数组,如：[2, 6, 4, 8, 10, 9, 15]，
    找出这个数组的最短子数组，当这个子数组排好序后，整个数组变为有序。
    这里的子数组为：[6, 4, 8, 10, 9]
    输出这个子数组的长度
    https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
    """

    def findUnsortedSubarray(self, nums):
        """
        :param nums:List[int]
        :return:int
        """
        nums_len = len(nums)
        if not nums or nums_len < 2:
            return 0

        end = 0
        start = nums_len - 1

        iter_range = range(nums_len-1)
        for i in iter_range:
            if nums[i+1] < nums[i]:
                end = i+1
                start = min(i, start)
                self.swap(nums, i, i+1)

        for i in reversed(iter_range):
            if nums[i] > nums[i + 1]:
                self.swap(nums, i, i + 1)
                start = min(start, i)

        return max(end - start + 1, 0)

    def swap(self, nums, a, b):
        """
        :param nums: List[int]
        :param a: int
        :param b: int
        :return: void
        """
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp

