"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
#算法思路：类似于242题，用242的判断函数，对s字符串进行等大小截取，一个个的对比判断

#     def __init__(self):
#         self.dic = {}
#     def findAnagrams(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: List[int]
#         """
#
#         for i in p:
#             if i not in self.dic:
#
#                 self.dic[i] = 1
#
#             else:
#                 self.dic[i] += 1
#         ls =[]
#         lenth = len(p)
#         for i in range(0, len(s)-lenth+1):
#             if self.isAnagram(p, s[i:i+lenth]):
#                 ls.append(i)
#
#         return ls
# #直接调用242的函数，重复创建了p的dict，简花步骤，可以给p创建一个dict，然后在比较
#
#     def isAnagram(self,  t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#
#         for i in t:
#             if i not in self.dic:
#                 return False
#             else:
#                 self.dic[i] -= 1
#         for key in self.dic:
#             if self.dic[key] != 0:
#                 return False
#         return True
#######上面的算法耗时太长ac不过，尴尬，相当于每次判断都得创建一个dict，麻烦。换个思路创建两个dict，比对两个dict是否一样
# 只用一个dict，在这个dic上增删，就不用每次都重复创建dic
# 还能改进，看不下去了http://bookshadow.com/weblog/2016/10/23/leetcode-find-all-anagrams-in-a-string/
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ds = collections.Counter()
        dp = collections.Counter(p)
        rlist =[]
        ls = len(s)
        lp = len(p)
        for i in range(0,ls):
            ds[s[i]] += 1
            if i>=lp:
                ds[s[i-lp]] -=1
                if ds[s[i-lp]] ==0:
                    del ds[s[i-lp]]

            if ds ==dp:
                rlist.append(i-lp+1)
        return rlist
