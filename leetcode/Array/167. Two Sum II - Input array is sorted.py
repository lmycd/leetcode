"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

# 算法思路：两个指针，不需要全部走全，因为已经排序了

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 时间超时了 严格地说这个暴力算法的时间复杂度是o(n的平方)
        # for i in range(0, len(numbers)):
        #     sol = target - numbers[i]
        #     for j in range(i+1, len(numbers)):
        #         if sol == numbers[j]:
        #             return [i, j]
        #         elif numbers[j] > sol:
        #             break
        #

        #用二分搜索法时间复杂度o（nlogn）,寻找sol的时候可以用二分搜索，不必暴力匹配
        # for i in range(0, len(numbers)):
        #     sol = target - numbers[i]
        #     index = (i + 1 + len(numbers) - 1) / 2
        #     while sol != numbers[index]:
        #
        #         if sol == numbers[index]:
        #             return [i+1,index+1]
        #         elif sol < numbers[index]:
        #             index = (i+1 + index)/2
        #         else:
        #             index =(index + len(numbers)-1)/2
        #     return [i+1, index+1]

       #  用两个指针，左，右指针，左右；两个数想加小于target，则左指针+1，否则右指针-1，遍历一遍，时间复杂度o（n）
        left, right = 0, len(numbers)-1
        while left <= right:
            if numbers[left] +numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1



