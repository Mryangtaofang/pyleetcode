

class Solution:
    """
    Unique Paths

    https://leetcode.com/problems/unique-paths/
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0

        if m > n:
            tmp = m
            m = n
            n = tmp

        dp = [1 for i in range(m)]

        for y in range(1, n):
            for x in range(1, m):
                dp[x] += dp[x-1]

        return dp[m-1]
