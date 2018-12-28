#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    斐波那契数列
    """
    def solution(self, num):
        result = [0, 1]
        for index in range(num):
            result.append(result[-2] + result[-1])

        return result


solution = Solution()
print(solution.solution(8))
