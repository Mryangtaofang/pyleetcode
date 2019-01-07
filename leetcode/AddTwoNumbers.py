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
        if not l1:
            return l2

        if not l2:
            return l1

        result = ListNode(0)
        cur = result
        last_num = 0
        while l1 or l2:
            l1_num = l1.val if l1 else 0
            l2_num = l2.val if l2 else 0

            total = l1_num + l2_num + last_num
            if total >= 10:
                last_num = 1
                total -= 10
            else:
                last_num = 0

            cur.next = ListNode(total)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if last_num > 0:
            cur.next = ListNode(last_num)

        return result.next
