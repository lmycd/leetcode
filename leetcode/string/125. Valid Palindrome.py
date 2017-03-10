"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""
# 算法思路：两个指针，从前往后和从后往前。对与每个字符判断其是否是字母或者数字,是就比较是否相等，如果不是指针往移动

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s)-1
        while i <= j:
            # 防止字符串的index越界 ，所以要加上 and 后面的条件
            while not (s[i].isalpha() or s[i].isdigit()) and i < len(s)-1:
                i += 1
            while not(s[j].isalpha() or s[j].isdigit()) and j >= 0:
                j -= 1
            if i <= j:
            ##都变为小写
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False

        return True
