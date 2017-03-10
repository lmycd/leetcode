"""Given an integer, write a function to determine if it is a power of two."""



# 算法思路：考虑问题 n=0 n为负数 ，考虑全面点
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n:
            if n % 2 and n/2 != 0:
                return False
            n = n/2
        return True

#用按位与的方法
    def isPowerOfTwo(self, n):
        return n &(n-1) == 0