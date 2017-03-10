"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""

# 算法思路 桶排序
# 无论哪种方法都要遍历一边数组，关键在于窗口k里面的比较。在窗口k里，最多有k个桶，只要当前值能放在现存的桶里，true，不能看左右的桶的值。一个桶里面
# 只有一个值，判断下。都不行就创建个桶。！！！！！打败百分之九十的提交者


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """

        #t为负数，返回false，t应该为正数
        if t <0:return False

        div = t+1
        tong = {}
        for i, value in enumerate(nums):
            index = value/div
            if index in tong \
                    or index-1 in tong and abs(tong[index-1]-value) <= t \
                    or index+1 in tong and abs(tong[index+1]-value) <= t:
                return True
            tong[index] = value
            #当i为k，比对完，就得在桶中删掉下标为0的数，因为下次循环是下标为k+1，窗口大小为k，所以起始下标为1
            if i >= k:
                del tong[nums[i-k]/div]
        return False



