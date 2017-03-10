"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods? Show More Hint

"""


class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        stack = []
        while num:
            stack.append(num % 10)
            num = num/10
        a=0
        for i in stack:
            a += i
        if a <10:
            return a
        else:
            self.addDigits(a)