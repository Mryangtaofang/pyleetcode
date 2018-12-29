#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    https://leetcode.com/problems/merge-intervals/
    """
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        stop = True
        index = 0
        while index < len(intervals):
            while stop:
                stop = self.__merge_one(intervals, index)

            index += 1
            stop = True
        return intervals

    def __merge_one(self, intervals, index):
        head = intervals[index]

        index += 1
        while index < len(intervals):
            new_item = intervals[index]
            if head.start <= new_item.start <= head.end:
                head.end = head.end if new_item.end < head.end else new_item.end
                intervals.remove(new_item)
                return True

            elif head.start <= new_item.end <= head.end:
                head.start = head.start if new_item.start > head.start else new_item.start
                intervals.remove(new_item)
                return True

            elif new_item.start < head.start and head.end < new_item.end:
                head.start = new_item.start
                head.end = new_item.end
                intervals.remove(new_item)
                return True
            else:
                index += 1

        return False

    def merge2(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ") "


# 测试
solution = Solution()
inters = solution.merge([Interval(2, 3),
                        Interval(2, 2),
                        Interval(3, 3),
                        Interval(1, 3),
                        Interval(5, 7),
                        Interval(2, 2),
                        Interval(4, 6)])

for inter in inters:
    print(inter)
