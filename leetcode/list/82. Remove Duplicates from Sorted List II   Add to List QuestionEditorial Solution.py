"""Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""
#算法思路：两个指针指向当前和下一个比较两者的val，引入count，计数有几个val相等，如果有0个相等的把当前的指针添加在新头节点的后面

#然后两个指针往后移动一位，直到靠右的指针为空

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
        dummy.next = None
        p = dummy

        while head:

            count = 0
            cur = head
            head = head.next
            while head and head.val ==cur.val :
                count += 1
                head = head.next

            if count == 0:
                p.next = cur
                cur.next = None
                p = p.next

        return dummy.next







