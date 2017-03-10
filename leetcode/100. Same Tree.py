"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

"""
算法思路：递归，4种情况：节点都为空：true，一空一不空，false，都不空则比较val，不同false，返回子节点的对比情况
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q ==None:
            return True
        else:
            if p == None and q != None:
                return False
            else:
                if p != None and q == None:
                    return False
                else:
                    if p.val != q.val:
                        return False
                    else:

                        return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)
