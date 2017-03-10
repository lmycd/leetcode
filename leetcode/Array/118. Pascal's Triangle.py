"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

注意：函数名重名，主函数没有返回值。写代码的逻辑一定要对。要全。想好了在写

"""


class Solution(object):
    def __init__(self):
        self.ls = []
        self.temp = []
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        for i in range(1,numRows+1):
            self.ls.append(self.generatet(i))
        return self.ls
    def generatet(self,num):

        if num == 1:
            return [1]
        if num ==2 :
            return [1,1]
        if num >2:
            #不能在这里吃书画temp因为下一行代码 会调用self.temp，temp保留了上一行的数字
           # self.temp =[]
            last = self.generatet(num-1)
            #得家在这儿
            self.temp = []
            self.temp.append(1)
            for i in range(0,len(last)-1):
                self.temp.append(last[i]+last[i+1])
            self.temp.append(1)
        return self.temp