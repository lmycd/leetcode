"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

算法思路：1卡特兰数，直接用公式。2动态规划。dp【n】=以n个数中的一个为根的所有可能树的数量集合。以某个数为根的bst数=dp【左】*dp【右】
可以直接列出一个推倒式子
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 2]
        if n<= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n+1):
                #dp[i]代表有i个节点的bst个数
                for j in range(i):
                    dp[i] += dp[j]*dp[i-1-j]

        return  dp[n]