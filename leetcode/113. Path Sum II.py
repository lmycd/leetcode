"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

#在类里面创建一个私有变量：存放满足条件的list，每做一次递归，就复制当前的添加了节点的list
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path=[]
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ls=[]
        x= self.pathSumHelper(root, sum, ls)
        print(x)
        return x

    def pathSumHelper(self, root, sum, ls):
        if not root:
            return False
        ls.append(root.val)
        if not root.left and not root.right and root.val == sum:
            self.path.append(ls)

        newls = ls[:]
        self.pathSumHelper(root.left, sum-root.val, newls)
        newls1 = ls[:]
        self.pathSumHelper(root.right, sum-root.val, newls1)

if __name__=="__main__":
    c = Solution()
    c.pathSum()




