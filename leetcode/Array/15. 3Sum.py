"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
算法思路：
"""
import collections
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        s =set([])
        for i in range(0, len(nums)):
            sum = 0 - nums[i]
            dic = {}
            for j in range(i+1, len(nums)):

                if nums[j] in dic and not self.panduan(res, [nums[i], nums[j], nums[dic[nums[j]]]]):
                        res.append([nums[i], nums[j], nums[dic[nums[j]]]])

                else:
                    dic[sum - nums[j]] = j
        return res

    def panduan(self,res,ls):
        for i in res:
            if set(i) ==set(ls):
                return True
