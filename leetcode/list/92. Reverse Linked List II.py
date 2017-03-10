"""Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
#需要逆序的部分用头插法，计数，记位置
        count =1
        dummy = ListNode(0)
        dummy.next = None
        p = dummy
        q =None

        while count<=n:
            if count<m:

                p.next = head
                p =p.next
                head = head.next
            if count>=m and count <=n:
                p.next = head
                cur = head.next
                head.next =q
                q = head
                head = cur
            count+=1

        if count > n:
            while q.next:
                q = q.next
            q.next = head
        return dummy.next












