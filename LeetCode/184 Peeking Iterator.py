# -*- coding: utf-8 -*-

'''
Peeking Iterator
================

Given an Iterator class interface with methods: next() and hasNext(), design
and implement a PeekingIterator that support the peek() operation -- it
essentially peek() at the element that will be returned by the next call to
next().

Here is an example. Assume that the iterator is initialized to the beginning of
the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after
that still return 2.

You call next() the final time and it returns 3, the last element. Calling
hasNext() after that should return false.

Follow up: How would you extend your design to be generic and work with all
types, not just integer?
'''


class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.cache = None

    def peek(self):
        if self.cache is None:
            self.cache = self.iter.next()
        return self.cache

    def next(self):
        if self.cache is not None:
            cache = self.cache
            self.cache = None
            return cache
        return self.iter.next()

    def hasNext(self):
        return self.iter.hasNext() if self.cache is None else True
