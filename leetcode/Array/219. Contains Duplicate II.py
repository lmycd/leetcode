"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

# 算法思路：不要陷入思维定势，可以用o（k*n）的复杂度来做，麻烦。
# 建立一个哈希表，不要思维定势，value可以不是个数。value可以是下标

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(nums):
            index = dic.get(v)
            if index is not None and i - index <= k:
                return True
            #update v's index
            dic[v] = i
        return False

