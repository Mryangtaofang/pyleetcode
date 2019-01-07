#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    https://leetcode.com/problems/convert-bst-to-greater-tree/
    """
    sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            self.convertBST(root.right)
            self.sum += root.val
            root.val = self.sum
            self.convertBST(root.left)

        return root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
