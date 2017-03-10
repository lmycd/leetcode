"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
#算法思路：每一个叶子节点对应一条路径，同时对应一个高度。所有的高度放入一个list中，取最大值。dfs递归，每天次都有一个参数表示当前的高度，
#同时复制当前高度，传入子节点的递归。代码执行速度超过大部分人应该是因为，用了空间换取时间。每次递归都会新建一到两个变量

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.depthA = []
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        self.dfs(root, depth)
        return max(self.depthA)
    def dfs(self,root,depth):
        if not root:
            return 0
        else:
            depth+=1
        if not root.left and not root.right:
            self.depthA.append(depth)
        newdepth = depth
        self.dfs(root.left, newdepth)
        newdepth1 = depth
        self.dfs(root.right, newdepth1)



