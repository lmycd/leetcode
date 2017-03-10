"""Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""
# 算法思路：1、哈希表，建造一个字典，key为字母，值是次数 。2、排序，拍完序对比下就行了

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i in s:
            if i not in dic:

                dic[i] = 1

            else:
                dic[i] += 1
        for i in t:
            if i not in dic:
                return False
            else:
                dic[i] -= 1
        for key in dic:
            if dic[key] != 0:
                return False
        return True