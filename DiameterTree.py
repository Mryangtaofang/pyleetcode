#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Solution:
    """
    https://leetcode.com/problems/diameter-of-binary-tree/solution/
    """

    def __init__(self):
        self.diameter = 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.__max_depth(root)

        return self.diameter - 1

    def __max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_depth = self.__max_depth(root.left)
        right_depth = self.__max_depth(root.right)

        new_diameter = left_depth + right_depth + 1
        self.diameter = max(self.diameter, new_diameter)

        return max(left_depth, right_depth) + 1


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
