# -*- coding: utf-8 -*-

'''
Flatten 2D Vector
=================

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]

By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,2,3,4,5,6].
'''


class Vector2D(object):
    '''算法思路：

    利用内置的迭代器，当然也可以用 i, j 两个指针分别代表 row，colmun 来模拟
    '''
    def __init__(self, vec2d):
        self.i = iter(vec2d)

    def next(self):
        return self.val

    def hasNext(self):
        if not hasattr(self, 'j'):
            try:
                self.j = iter(self.i.next())
            except StopIteration:
                return False

        try:
            self.val = self.j.next()
        except StopIteration:
            del self.j
            return self.hasNext()

        return True


i = Vector2D([
  [1,2],
  [3],
  [],
  [4,5,6],
  []
])


while i.hasNext():
    print i.next()
