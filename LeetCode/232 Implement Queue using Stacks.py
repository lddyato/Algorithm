# -*- coding: utf-8 -*-

'''
Implement Queue using Stacks
============================

Implement the following operations of a queue using stacks.

  - push(x) -- Push element x to the back of queue.
  - pop() -- Removes the element from in front of queue.
  - peek() -- Get the front element.
  - empty() -- Return whether the queue is empty.

Notes:

- You must use only standard operations of a stack -- which means only push to
  top, peek/pop from top, size, and is empty operations are valid.

- Depending on your language, stack may not be supported natively. You may
  simulate a stack by using a list or deque (double-ended queue), as long as
  you use only standard operations of a stack.

- You may assume that all operations are valid (for example, no pop or peek
  operations will be called on an empty queue).
'''


import collections


class Queue(object):
    def __init__(self):
        self._input = collections.deque()
        self._output = collections.deque()

    def push(self, x):
        self._input.append(x)

    def pop(self):
        self.peek()
        self._output.pop()

    def peek(self):
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())

        return self._output[-1]

    def empty(self):
        return not (bool(self._input) or bool(self._output))


queue = Queue()

queue.push(1)
queue.push(2)

print queue.peek()
queue.pop()
print queue.peek()
