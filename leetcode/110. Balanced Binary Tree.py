"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
#思路：左子树的高度与右子树的高度之差<1.写一个dfs遍历得到左右子树的高度

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))> 1:
             return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)



#######!!!!!!!!!递归求树的高度
    def height(self,root):
        if not root:
            return 0
        return  max(self.height(root.left),self.height(root.right))+1



    def res(self,root):
        """
        #返回当前节点的左右子树的高度之差的绝对值
        :param root: TreeNode
        :return: bool
        """
        if not root:
            return False
        return abs(self.maxDepth(root.left)-self.maxDepth(root.right))


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

