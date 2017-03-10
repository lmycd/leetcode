"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 尴尬 505ms 估计倒数第一的执行时间
        # 分治法
        if len(nums) == 1:
            return nums[0]

        left = self.maxSubArray(nums[:len(nums) // 2])
        right = self.maxSubArray(nums[len(nums)//2:])

        # 数组的下标
        lmix = nums[len(nums[:len(nums)//2]) - 1]
        lcur = nums[len(nums[:len(nums)//2]) - 1]
        for i in range(len(nums[:len(nums)//2])-2, -1, -1):
            lcur += nums[i]
            lmix = max(lmix, lcur)
        # 这里的数组的下标要注意
        rmix, rcur = nums[len(nums)//2], nums[len(nums)//2]
        for i in range(len(nums)//2+1, len(nums)):
            rcur += nums[i]
            rmix = max(rmix, rcur)


        print(left,right,rmix,lmix)
        return max(left, right, rmix+lmix)


s = Solution()
print(s.maxSubArray([8,-19,5,-4,20]))