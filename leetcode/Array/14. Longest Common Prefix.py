




#将第一个字符串与其他所有字符串比较，所求的是最小的公共前缀
##

# 提升： 用长度最短的字符串作为基准，这样的话返回的最长的长度都不会大于该字符串的长度。
# 之前的横向一个个比较其实麻烦。没必要全部比较。不如纵向比较，都选第一个字母比较，只要有不同就返回当前的字符串。若比较完没不同就返回最短的字符串
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #dic = {}
        if strs==[]:return ''
        f = min(strs)
        for i in range(len(f)):
            for s in strs:
                if s[i] != f[i]:
                    return f[:i] if i > 0 else ''
        return f

        # dict = sorted(dic.items(), key=lambda d: d[1], reverse=True)
        # return dict[-1][0]
