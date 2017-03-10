"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# 算法思路：c表示进位,考虑问题要细致，所有情况都考虑进去，思路要对

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []
        #c 表示进位
        c = 0
        while l1 or l2:
            if not l1:
                res.append((l2.val+c)%10)
                #每做一次加法运算都要考虑进位，并且记录进位
                c = (l2.val+c)//10
                l2 = l2.next

            elif not l2:
                res.append((l1.val+c)%10)
                c = (l1.val+c)//10
                l1 = l1.next
            else:
                #
                #res.append((l1.val + l2.val) % 10 + c)
                res.append((l1.val + l2.val+c) % 10)
                c = (l1.val + l2.val+c)//10

                l1, l2 = l1.next, l2.next
        if c:
            res.append(c)
        return res