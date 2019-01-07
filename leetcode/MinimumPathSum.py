

class Solution:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.

    Example:

    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.
    https://leetcode.com/problems/minimum-path-sum/
    """
    def minPathSum(self, nums):
        if not nums:
            return 0

        dp = []

        for y in range(len(nums)):
            for x in range(len(nums[0])):
                if y:
                    if x:
                        dp[y].append(min(dp[y-1][x], dp[y][x-1]) + nums[y][x])
                    else:
                        dp.append(list(dp[y-1][x] + nums[y][x]))
                else:
                    if x:
                        dp[y].append(dp[y][x-1] + nums[y][x])
                    else:
                        dp.append(list(nums[y][x]))

        return dp[-1][-1]
