"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
实现一个迭代器
算法思路：二叉搜索树：中序遍历得到序列，用栈来存储，迭代器的实现需要，没运行一次函数产生一个新的next最小值。进栈的是最左的节点
对当前点的操作，然后要对该节点的右子节点操作。如果没有右节点，则栈中弹出节点。重复此操作。进栈的顶部最小，出战后的操作后，下一个就是右子节点
没有右自节点就，选上层节点
"""


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.cur = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0 or self.cur is not None

    def next(self):
        """
        :rtype: int
        """
        #while循环中序遍历，最总要的是运行一次返回一个最小值
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        nxt = self.cur.val
        self.cur = self.cur.right
        return nxt



        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())