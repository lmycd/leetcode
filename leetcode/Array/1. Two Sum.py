"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # target为8，第一个数为4 ，gg，找到自己
        # for i in nums:
        #     if target-i in nums:
        #         return [nums.index(i), nums.index(target-i)]
        # 另一种方法，hash表
        dic = {}
        for i in range(0, len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target-nums[i]] = i


