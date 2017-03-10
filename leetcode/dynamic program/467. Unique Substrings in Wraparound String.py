"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""
#算法思路：寻找以某个字母结尾的最长连续（子串可以覆盖短的序列的子串）的子序列，以这个字母结尾的子串的个数就是其长度。
# cmap代表字典，key为字母，value为以key结尾的最长连续字符串的长度
#遍历字符串，判断当前字母和前一个字母是否是连续的字符串（可以直接用自字符串是否在 pattern里找到来判断），如果是，则以当前字母为末尾字母的字符串的长度加1





from collections import defaultdict

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        pattern = "zabcdefghijklmnopqrstuvwxyz"
        cmap = defaultdict(int)
        clen = 0
        for i in range(len(p)):
            if i and p[i-1:i+1] in pattern:
                clen += 1

            else:
                clen = 1
            cmap[p[i]] = max(clen, cmap[p[i]])
        return sum(cmap.values())