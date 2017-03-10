"""
算法思路：正序找下标，将字符串逆置，找下标。如果下标相加再加1等于字符串的长度则代表，找到了第一个唯一的字符
!!!!!!!!!!!!for index, i in enumerate(ls):遍历数组的同时，获取下标。判断条件：字符的下标和index（）返回的找到的第一个下标是否相同
再加上上面一行的条件，
"""



# """
# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s:
#             return -1
#         ls = list(s)
#         rls = list(reversed(ls))
#         for index, i in enumerate(ls):
#             # print(index)
#             # print(i)
#             lindex = ls.index(i)
#             rindex = rls.index(i)
#             if lindex == index and index == len(ls) - 1 - rindex:
#                 return index
#             elif index == len(s)-1:
#                 return -1
#
# if __name__ =="__main__":
#     exe = Solution()
#     print(exe.firstUniqChar("acccddsda"))
# """
"""
创建一个哈希表可以用dict表示key为字符串的字符，value为出现的次数
寻找次数为1的key，比较他们的index，返回最小的index
！！！！！！！！！这个方法的速度比上一个方法快很多。
"""



class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}
        ls=list(s)
        for i in ls:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        a = []
        for key in dic:
            if dic[key]==1:
                a.append(key)
        if not a:
            return -1

        return min([ls.index(i) for i in a])

if __name__ == "__main__":

    exe = Solution()
    print(exe.firstUniqChar("leetcode"))
