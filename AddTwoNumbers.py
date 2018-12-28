#!/usr/bin/python
# -*- coding: UTF-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        result = ListNode(0)
        cur = result
        last_num = 0
        while l1 is not None or l2 is not None:
            l1_num = l1.val if l1 is not None else 0
            l2_num = l2.val if l2 is not None else 0
            total = l1_num + l2_num + last_num
            if total >= 10:
                last_num = 1
                total -= 10
            else:
                last_num = 0

            cur.next = ListNode(total)
            cur = cur.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if last_num > 0:
            cur.next = ListNode(last_num)

        return result.next
