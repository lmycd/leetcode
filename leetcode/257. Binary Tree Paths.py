"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#算法思路：递归实现，安利的输出。可以用list表示，然后用.join拼接成字符串"->"用这个拼接更方便，！！！join必须本身是字符串
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def __init__(self):
        self.path = []

    def binaryTreePaths(self, root):
        ls = []
        self.add(root, ls)
        return self.path

    def add(self,root,ls):
        if not root:
            return
        ls.append(root.val)
        if root.left or root.right:
            ls.append("->")
        else:
            #self.path.append("".join(ls)) :报错 ls的元素有的是数字
            self.path.append("".join(str(i) for i in ls))
        newls1 = ls[:]
        self.add(root.left, newls1)
        newls2 = ls[:]
        self.add(root.right, newls2)

