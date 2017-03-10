"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
#算法思路：hashtable，计数（暴力解法）
# 分治：
import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1、排序nlog（n），>>右移，相当于除以2
        #return sorted(num)[len(num) >> 1]

        #2、哈希表时间o（n），空间o（n）
        numsdic = collections.Counter(nums)
        lenth = len(nums)
        for key in numsdic:
            if numsdic[key] >= lenth/2:
                return key


class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #3、摩尔投票o（n），空间o（1）：1、用一个计数器计数，当计数器为0的时候，候选元素换称当前元素， 与当前相同计数器加1，否则减一
        #2、在遍历一次看看主元素是否合法
        #！！！！1https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
        candidate = cnt = 0
        for num in nums:
            if candidate ==num:
                cnt += 1
            elif cnt:
                cnt -= 1
            if cnt == 0:
                candidate, cnt = num, 1
        return candidate

        #4、分治法，基本情况为数组只有一个元素，则返回当前元素，合并的时候如果两个元素相同，就返回同的，如果不同就返回占元素多的.

            #基本情况数组元素为1。 合并的时候，需要对当前数组对子数组返回的最大值数进行次数计算，大于一半就返回那个值，否则返回另一个值。比如就两个不同的数，几乎随机返回一个。调用count方法。这个时间复杂度就不低了这样的话
    # 就不会出错了
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #
        if len(nums)==1:
            return nums[0]
        if not nums:
            return None
        a = self.majorityElement1(nums[:len(nums)//2])
        b = self.majorityElement1(nums[len(nums)//2:])
        if a ==b :return a
        if nums.count(a)>len(nums)//2:return a
        else:return b