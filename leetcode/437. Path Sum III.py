"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
"""
算法思路：相当于对每个节点做dfs，且sum=8，而针对某个节点的时候利用dfs，寻找sum=8：相当于两层递归：外层用来递归的寻找解，另外一层寻找递归找解
dfs是对一个根节点找路径和是sum的递归，将这个递归用在每个节点上，就能递归得到所有的解
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #判断跟节点是否为空
        if not root:
            return False
        self.dfs(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.res
    def dfs(self,root,sum):
        if not root:
            return False
        if sum == root.val:
            self.res = self.res+1
        self.dfs(root.left, sum-root.val)
        self.dfs(root.right, sum-root.val)