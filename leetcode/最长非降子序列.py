# 最长非降子序列


def ma(ls):
    # res[i]代表以i结尾的的最长子序列的长度
    res = [1 for i in range(len(ls))]
    maxlen = 1
    for i in range(1, len(ls)):
        for j in range(0, i):
            if ls[i] >= ls[j]:
                res[i] = max(res[i], res[j]+1)
        # 求解长度为n的最长子序列等于以数组中的每个元素结尾的最长子序列中长度的最大值
        maxlen = max(maxlen, res[i])
    return maxlen
if __name__ == "__main__":
    print(ma([4,2,5,1,9,3,7,11,12,10]))
    # 合格：算法对的
    # 就是以每个