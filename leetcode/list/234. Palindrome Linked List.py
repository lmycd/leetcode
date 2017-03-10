"""Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?"""
##两个指针，快指针一次跑两个节点，慢指针一次一个，当快指针跑到顶时，满指针才跑到中间。得到中间的位置，满指针走的值存入栈中

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.stack = []
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        p =head

        self.stack.append(head.val)
        ##!!!!!p.next结束对应奇数个节点」||p.next.next对应于偶数个节点，即倒数第二个结束点
        while p.next and p.next.next:
            p =p.next.next
            head = head.next
            self.stack.append(head.val)
        if p.next == None:

            while self.stack:
                if self.stack.pop() ==head.val:
                    head =head.next
                else:
                    return False
        else:
            while self.stack:
                head = head.next
                if self.stack.pop() ==head.val:
                    continue
                else:
                    return False
        return True

