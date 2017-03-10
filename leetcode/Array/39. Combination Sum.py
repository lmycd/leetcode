"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

###回溯法就靠栈来实现：进栈即往下层走，出栈即回退到上个版本
class Solution(object):

    def __init__(self):
        self.ret = []
        self.canlist = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #这个j用来避免重复的解出现：比如第一层循环第二个数进栈，就代表第一个数之后没必要再用了，因为前面在第一个数进栈的时候，包含第一个数的所有可能解
        ##都有了。所以要想办法把前面的数去掉。
        ##我想出了 添加变量j，用来调整candidates里的元素：原以为不成功的，因为感觉j会随着层数的增大，j数量会太大。
        ##后来观察发现，没进入下一层，j的初始值都为0啊，这样的话就可以用j：list的第几个元素  来控制candidates的元素，避免选择重复的元素，
        ###避免重复解。美滋滋
        j=0
        for i in candidates:

            if i == target:
                #候选栈的元素是靠出栈，来更新的不是靠初始化
                # 进栈
                self.canlist.append(i)
                self.ret.append(self.canlist[:])
                # 出栈
                self.canlist.pop()

            elif target-i > 0:
                # 元素进栈
                self.canlist.append(i)
                self.combinationSum(candidates[j:], target-i)
                #元素出栈
                self.canlist.pop()
            j += 1
        return self.ret


