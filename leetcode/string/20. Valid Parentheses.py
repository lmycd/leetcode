"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
#!!!!栈
##这个没法用两个指针做，因为右边对应的可能就在下一个，只能用栈来做，左符号全部入栈，遇到右符号出栈比较,最后判断栈是否为空,空就代表ture，不空返回false
class Solution(object):
    def __init__(self):
        self.stack =[]
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in s:
            if i == "[" or i =="{" or i =="(":
                self.stack.append(i)
            else:
                if len(self.stack):
                    current = self.stack.pop()
                else:
                    return False
                if i =="}" and current != "{":
                    return False
                if i =="]" and current != "[":
                    return False
                if i ==")" and current != "(":
                    return False
        if not len(self.stack):
            return True






