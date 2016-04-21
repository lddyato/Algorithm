# -*- coding: utf-8 -*-

'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be
integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,4,6].
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    '''算法思路：

    DFS遍历，得到所有的数据
    '''
    def __init__(self, nestedList):
        self.r = []
        self.i = 0
        self.dfs(nestedList)

    def dfs(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.r.append(item.getInteger())
            else:
                self.dfs(item.getList())

    def next(self):
        result = self.r[self.i]
        self.i += 1
        return result

    def hasNext(self):
        return self.i < len(self.r)


class NestedIterator(object):
    '''算法思路:

    不预先生成要遍历的序列，而是再遍历的时候生成
    '''
    def __init__(self, nestedList):
        self.stack = []
        self.iter = iter(nestedList)

    def next(self):
        return self.nextInteger

    def hasNext(self):
        while self.iter:
            try:
                r = self.iter.next()
            except StopIteration:
                self.iter = self.stack.pop() if self.stack else None
                continue

            if r.isInteger():
                self.nextInteger = r.getInteger()
                return True

            self.stack.append(self.iter)
            self.iter = iter(r.getList())
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
