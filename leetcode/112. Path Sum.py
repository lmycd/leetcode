"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#算法思路：递归：一个节点为空，返回null，一个节点，左右节点为空，判断是否与sum的值一样。否则递归左右子树
#!!!!!类中递归调用函数需要用self
"""
递归：对于树而言
"""



class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.value
        return self.hasPathSum(root.left, sum-root.value) or self.hasPathSum(root.right, sum-root.value)


