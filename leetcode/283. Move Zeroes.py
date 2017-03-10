"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a=0
        for i in range(len(nums)):
            if nums[i ]==0:
                a += 1
            else:
                nums[i-a]= nums[i]
                #del nums[nums.index(i)]


        for i in range(a):
            nums[len(nums)-i-1] = 0
"""
报错原因：删除一个元素后，列表整体迁移，第二个0向前移占剧当前迭代的位子，就意味着跳过了该元素，因为此位置的元素已经迭代过了，1往迁移，迭代就从1开始
Submission Result: Wrong Answer More Details

Input:
[0,0,1]
Output:
[0,1,0]
Expected:
[1,0,0]"""