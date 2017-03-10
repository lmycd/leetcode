"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
# 算法思路：pn代表阶梯为n的时候，有多少种走法，pn=pn-1 + pn-2
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #在n为35 时间超了
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        # 用迭代
        if n<=2:
            return n
        result = [1,2]
        for i in range(n-2):
            result.append(result[-1]+result[-2])
        return result[-1]