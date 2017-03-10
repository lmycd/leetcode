"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
##思路：循环一次，计节点数，这样就知道遍历应该在哪里停止!!!!!!注意[1],1的情况，最好应该把头节点带上遍历，这样就不需要单独判断这种情况了
#指扫描一遍的话，就需要算出位置。就用两个指针。第一个指针到n的位置停止。然后和第二个指针（从头）一起开始，当第一个指针到头的时候
        #第二个指针就到了应该到的位置
        dummy = ListNode(0)
        dummy.next, count = head, 0
        p =dummy
        if head.next == None and n==1:
            return []


        while head:
            head, count = head.next, count+1
        cnt = 0
        while cnt < count - n :
            p = p.next
            cnt += 1
        p.next =p.next.next
        return dummy.next

