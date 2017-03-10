"""

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #每次遍历到最后一个节点，
        # dummy = ListNode(0)
        # dummy.next = head
        # q = dummy
        # #dummy1新联表的头节点
        # dummy1 = ListNode(0)
        # p = dummy1
        #
        # while q.next:
        #     while q.next.next :
        #         q = q.next
        #     p.next = q.next
        #     p = p.next
        #     q.next = None
        #     q = dummy
        # return dummy1.next

# 头插法可以很好的解决问题不需要每次都遍历到最后的节点

        dummy = ListNode(0)
        dummy.next = None
        p = None
        cur = head

        while head:
            # 这种写法会节省时间，大大减少运行时间
            dummy.next, head.next, head, p = head, p, head.next, head

        return dummy.next







