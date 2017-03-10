"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.
"""

###两种情况：截取不同的字符串，两个指针，左指针负责不重复字符串的开头，右指针负责一个个的添加字符，然后与已存在的子字符串比较，有相同则截取，无则继续舔埃及
##### 特殊情况：添加到结尾时当前子串就是个带候选的子串。 注意字典得时刻更新对应当前的子串：llpoint记录上次的lpoint，这样就删除两个指针之间的字典元素
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        candidate = []
        lpoint, llpoint, rpoint = 0, 0, 0
        lenth = len(s)
        while rpoint < lenth:
            if s[rpoint] not in dic:
                dic[s[rpoint]] = rpoint
                #####忘记考虑没有相同字符的情况了：没有相同字符的话就直接返回
                if rpoint == lenth-1:
                    candidate.append(rpoint-lpoint+1)
            else:
                candidate.append(rpoint-lpoint)
                lpoint = dic[s[rpoint]]+1
                #报错，在迭代过程中不能删除元素，应该用pop（'元素'），删除简直对
                # for i in dic:
                #     if dic[i] < lpoint:
                #         del dic[i]
                for i in range(llpoint, lpoint):
                    dic.pop(s[i])

                llpoint = lpoint
                dic[s[rpoint]] = rpoint

            rpoint += 1
        if lenth == 1:
            return 1
        if lenth == 0:
            return 0
        return max(candidate)