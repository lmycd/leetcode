
"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
Subscribe to see which companies asked this question
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #创建一个集合，用set（）方法
        sets = set()
        for i in nums1:
            if i in nums2:
                sets.add(i)
        return list(sets)
#错误示范，得先创建一个类的实例，在用这个实例调用类的方法，这样就不会参数报错
# if __name__ == "__main__":
#     a = [2, 23, 2]
#     b = [2, 22, 1]
#
#     ls = Solution.intersection(a, b)
#     print(ls)
if __name__ == "__main__":
    a = [2, 23, 2]
    b = [2, 22, 1]
    c = Solution()
    ls = c.intersection(a, b)
    print(ls)


