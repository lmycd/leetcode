"""
中序遍历
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #递归的方法

    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if root is None:
    #         return []
    #     if root.left is not None:
    #         self.inorderTraversal(root.left)
    #     self.ls.append(root.val)
    #     if root.right is not None:
    #
    #         self.inorderTraversal(root.right)
    #
    #
    #
    #     return self.ls


##非递归的方法，while循环
    def __init__(self):
        self.ls = []

        self.stack =[]


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.next(root)
        return self.ls


    def next(self, root):
        while root is not None or len(self.stack)>0:
            #找左节点
            while root is not None:
                self.stack.append(root)
                root = root.left

            #弹出中节点
            cur =self.stack.pop()
            self.ls.append(cur.val)
            #找右节点
            root = cur.right