"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?

"""
# 算法思路：二进制表示...pow2表示大于当前数的2的幂次方，before表示略小于当前数的2的幂次方，res代表返回的list，res[i] =res[i-before]+1
# i-before肯定是小于当前i的，所以res[i-beforce]肯定是已知的。 举例res[7] =res[4]+res[3],4:二进制在最高位，3在低位互不不干扰
# 动态规划：重点找到状态转移的递推式子，就行了
#速度打败百分之80的人


import collections
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num ==0:
            return [0]
        res = [0]*(num+1)
        pow2 =before =1
        for i in range(1, num+1):
            if i == pow2:
                before =pow2
                res[i] = 1
                pow2 <<=1
            else:

                res[i] = 1 + res[i-before]
        return res



