#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).

    Note: You may not engage in multiple transactions at the same time
    (i.e., you must sell the stock before you buy again).

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices and len(prices) < 2:
            return 0

        max_profit = 0
        for i in range(len(prices))[1:]:
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]

        return max_profit
