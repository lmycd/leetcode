"""Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from  collections import Counter

# 算法思路：hashtable，key为字符，value为次数，计数value的值大于等于2，有出现次数等于1的长度加一
#!!!!找出所有偶数和最大的奇数,count 记录偶数的和.错误！！！！！
#所有的奇数-1，加上1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdic ,count,maxodd= Counter(s) ,0 ,0
        for key in sdic:
            if sdic[key] %2 == 0:
                count += sdic[key]
            else:

                count +=sdic[key]-1
                maxodd =1
        return count+maxodd
