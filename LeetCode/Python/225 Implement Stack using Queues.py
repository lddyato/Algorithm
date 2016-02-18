# -*- coding: utf-8 -*-

'''
Implement Stack using Queues
============================

Implement the following operations of a stack using queues.

  - push(x) -- Push element x onto stack.
  - pop() -- Removes the element on top of the stack.
  - top() -- Get the top element.
  - empty() -- Return whether the stack is empty.

Notes:
- You must use only standard operations of a queue -- which means only push to
  back, peek/pop from front, size, and is empty operations are valid.

- Depending on your language, queue may not be supported natively. You may
  simulate a queue by using a list or deque (double-ended queue), as long as
  you use only standard operations of a queue.

- You may assume that all operations are valid (for example, no pop or top
  operations will be called on an empty stack).

Update (2015-06-11):

The class name of the Java function had been updated to MyStack instead of
Stack.
'''


import collections


class Stack(object):
    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        self._queue.append(x)
        for i in xrange(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not bool(self._queue)


a = Stack()
print a.empty()

a.push(1)
a.push(2)

print a.top()

a.pop()

print a.top()
