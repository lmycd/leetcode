"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

# 算法思路：用栈来匹配，匹配的括号在list中对应的位置为布尔值1，不匹配的为0，进栈的就是括号在字符串的下标，因为最重要得到的就是
### 成对括号的下标


###因为进栈的都是做括号，匹配的都是右括号，所以没必要用做括号进栈，让下标进栈
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        match = [0 for i in range(0,len(s))]
        stack = []
        for i , c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")" and len(stack):
                match[i] = match[stack[-1]] = 1
                stack.pop()

        cnt = 0
        res = 0
        for i in match:
            if i == 1:
                cnt += 1
                res = max(res, cnt)
            else:

                cnt = 0

        return res




