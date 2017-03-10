"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)
        index = start + (end - start) // 2
        while start <= end:

            if nums[index] == target:
                return index
            elif nums[index] > target:
                end = index - 1
                if end >= 0:
                    if nums[end] <= target:
                        return end+1
                else:
                    return 0

                index = start + (index - start)//2
                # if start == end:
                #     return index + 1
            else:
                start = index + 1
                if start <= len(nums):
                    if nums[start] >= target:
                        return start+1
                    else:
                        return len(nums)


                index = start + (end - start)//2


