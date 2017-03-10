class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ls = []
        for i in nums1:
            if i in nums2:
                ls.append(i)
                nums2.remove(nums2[nums2.index(i)])
        return ls


if __name__=="__main__":
    c = Solution()
    print(c.intersect([1, 2,2, 3], [1, 2]))
