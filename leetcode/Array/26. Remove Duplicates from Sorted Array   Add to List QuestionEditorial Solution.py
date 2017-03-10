"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


"""
"""
题目说不能分配额外的空间，我先用字典做一下
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ##我没注意list是有序的，当作无序来做的。最后一条测试用例没过。可能是包内存？超时间？
        # dic = {}
        # for i in nums:
        #     if i not in dic:
        #         dic[i] =1
        #     else:
        #         dic[i] += 1
        #
        # for key in dic:
        #     if dic[key] > 1:
        #         while dic[key] > 1:
        #             nums.remove(key)
        #             dic[key] -= 1
        # return len(nums)

        #写个简单点的：有序的话，就左右比较
        # i =0
        # while i <len(nums)-1:
        #     if nums[i] ==nums[i+1]:
        #         nums.remove(nums[i])
        #     else:
        #         i += 1
        # return len(nums)
        #


        #不删除元素
        count = 0
        i =0
        while i < len(nums):
            if i ==0 or nums[i] != nums[i-1]:

                nums[count] = nums[i]
                count+=1
        return count
