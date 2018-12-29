#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    """

    __result = [-1, -1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.__search(nums, target, 0, len(nums)-1)
        return self.__result

    def __search(self, nums, target, start, end):
        if end < start:
            return

        mid = (end + start) // 2

        if target == nums[mid]:
            index = self.__start_or_end(nums, target, mid)
            if index == -1:
                self.__search(nums, target, mid + 1, end)
            elif index == 1:
                self.__search(nums, target, start, mid - 1)
            else:
                self.__search(nums, target, mid + 1, end)
                self.__search(nums, target, start, mid - 1)

        elif target < nums[mid]:
            self.__search(nums, target, start, mid - 1)
        else:
            self.__search(nums, target, mid + 1, end)

    def __start_or_end(self, nums, target, index):
        if index == 0 or nums[index-1] != target:
            self.__result[0] = index
            return -1

        if index == len(nums) - 1 or nums[index + 1] != target:
            self.__result[1] = index
            return 1

        return 0


# 测试
solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 7))
