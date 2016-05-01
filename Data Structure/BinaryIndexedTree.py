# -*- coding: utf-8 -*-

'''
树状数组
======

理解树状数组的关键点在于，每个 combination，即 BIT[i] 为以 index=i 结尾，长为 i & (-i)
的和，这里实现上用了点 trick，即 index 从 1 开始计数，这样便于编码和理解

- i & (-i) 的含义是：i 的二进制中最后一个1所代表的数
- BIT[i] 与 他的左邻和父亲节点的距离为 i & (-i)，我们可以根据此特性来 update 和 query
- 树状数组一般用来统计数字出现的频率
- 与线段树之间的关系
  - 树状数组能够做的线段树也能够做，但线段树能够做的树状数组不一定能够做
  - 树状数组效率更高

参考这张图以便于理解：http://baike.baidu.com/pic/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84/313739/0/960a304e251f95ca5e588459cf177f3e660952ab?fr=lemma&ct=single#aid=0&pic=960a304e251f95ca5e588459cf177f3e660952ab
'''


class BinaryIndexedTree(object):
    def __init__(self, nums):
        self.nums = [0] + nums
        self.build()

    def build(self):
        self.BIT = [0] * len(self.nums)

        for i in range(1, len(self.nums)):
            for j in xrange(i, i - (i & (-i)), -1):
                self.BIT[i] += self.nums[j]

    def update(self, index, val):
        i = index + 1
        while i < len(self.nums):
            self.BIT[i] += val
            i += i & (-i)

    def query(self, index):
        i, r = index + 1, 0
        while i >= 1:
            r += self.BIT[i]
            i -= i & (-i)
        return r


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 100) for _ in range(100)]

    tree = BinaryIndexedTree(nums)

    assert tree.query(20) == sum(nums[:21])
    assert tree.query(99) == sum(nums)
