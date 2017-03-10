"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
# 算法思路： 深度优先搜索，条件：字符串里的左括号的数量比右括号多，左括号的数量不大于n
# 当左右括号的数量等于n的时候，返回一个成功的字符串
# 回溯法——深度优先搜索，递归的比较好写，


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ls = []
        str = []
        self.gen(0, 0, n, str, ls)
        return ls

    def gen(self, left, right, n, str, ls):
        if left == n and right == n:
            ls.append("".join(str))
            return
        #
        if left < n:
            # 进栈相当于进入下层结构
            str.append("(")
            self.gen(left + 1, right, n, str, ls)
            # gen函数结束，出栈相当于回到上层结构，回溯开始
            str.pop()
        if right < left:
            str.append(")")
            self.gen(left, right + 1, n, str, ls)
            str.pop()


