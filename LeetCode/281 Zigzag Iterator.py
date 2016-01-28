# -*- coding: utf-8 -*-

'''
Zigzag Iterator
===============

Given two 1d vectors, implement an iterator to return their elements
alternately.

For example, given two 1d vectors:

    v1 = [1, 2]
    v2 = [3, 4, 5, 6]

By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be
extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For
example, given the following input:

    [1,2,3]
    [4,5,6,7]
    [8,9]

It should return [1,4,8,2,5,9,3,6,7].
'''


class ZigzagIterator(object):
    '''算法思路：

    记录遍历指针即可，对于 k 个，只需把 self.arrays 改成对应的 arrays 即可
    '''
    def __init__(self, v1, v2):
        self.arrays = [v1, v2]
        self.lenArrays = len(self.arrays)

        self.arrayLengths = map(len, self.arrays)
        self.pointers = [0] * self.lenArrays

        self.total = sum(self.arrayLengths)
        self.count = 0
        self.cursor = 0

    def incrCursor(self):
        self.cursor = (self.cursor + 1) % self.lenArrays

    def next(self):
        while self.pointers[self.cursor] >= self.arrayLengths[self.cursor]:
            self.incrCursor()

        val = self.arrays[self.cursor][self.pointers[self.cursor]]
        self.pointers[self.cursor] += 1

        self.incrCursor()
        self.count += 1

        return val

    def hasNext(self):
        return self.count < self.total


i = ZigzagIterator([1, 2, 3], [4, 5, 6, 7])

while i.hasNext():
    print i.next()
