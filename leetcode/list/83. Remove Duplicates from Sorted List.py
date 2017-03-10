"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# 算法思路：两个指针,值相等就删除后面的节点，不同就都往后移动一位。水题
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy.next
        if p:
            head = head.next

        while head:
            if p.val == head.val:
                p.next, head = head.next, head.next
            else:
                p, head = head, head.next
        return dummy.next


