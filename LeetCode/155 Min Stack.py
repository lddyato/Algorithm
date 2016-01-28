# -*- coding: utf-8 -*-

'''
Min Stack
=========

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.
'''


class MinHeap(object):
    '''维护一个最小堆'''

    def __init__(self):
        self.array = []

    def heapify(self, start, end):
        father, son = start, start * 2 + 1
        while son <= end:
            if son + 1 <= end and self.array[son + 1] < self.array[son]:
                son += 1

            if self.array[son][0] > self.array[father][0]:
                break

            self.array[father], self.array[son] = (
                self.array[son], self.array[father])

            father, son = son, son * 2 + 1

    def insert(self, node):
        '''O(log(n))'''

        self.array.append(node)

        son = self.length - 1
        father = (son - 1) / 2

        while father >= 0 and self.array[son][0] < self.array[father][0]:
            self.array[father], self.array[son] = (
                self.array[son], self.array[father])
            son, father = father, (father - 1) / 2

    def remove(self, node):
        '''O(n)'''

        index = self.array.index(node)
        if index == self.length - 1:
            return

        self.array[index] = self.array.pop()
        self.heapify(index, self.length - 1)

    def top(self):
        return self.array and self.array[0] or None

    @property
    def length(self):
        return len(self.array)


class SortedArray(object):
    '''维护一个有序数组'''

    def __init__(self):
        self.array = []
        self.pointer = 0

    def binarySearch(self, node, exact=False):
        val, index = node
        low, high = 0, self.length - 1

        while low <= high:
            mid = (low + high) / 2

            if val > self.array[mid][0]:
                low = mid + 1
            elif not exact:
                if mid > 0 and val > self.array[mid - 1] or mid == 0:
                    return mid
                high = mid - 1
            elif val < self.array[mid][0]:
                high = mid - 1
            else:
                return mid
        return low

    def push(self, node):
        '''O(log(n))'''

        index = self.binarySearch(node)
        self.array.insert(index, node)

    def remove(self, node):
        '''O(log(n))'''

        self.array.pop(self.binarySearch(node, exact=True))

    def min(self):
        return self.array[0]

    @property
    def length(self):
        return len(self.array)


class MinStack(object):
    '''算法思路：

    用 arrary 来模拟 statck
    用最小堆来实现 getMin

    结果：TLE
    '''
    def __init__(self):
        self.array = []
        self.heap = MinHeap()

    def push(self, x):
        self.array.append(x)
        self.heap.insert((x, len(self.array)))

    def pop(self):
        self.heap.remove((self.array[-1], len(self.array)))
        self.array.pop()

    def top(self):
        return self.array and self.array[-1] or None

    def getMin(self):
        return self.heap.top()[0]


class MinStack(object):
    '''算法思路：

    维护一个有序数组，pop 的效率会比最小堆的高

    结果：AC
    '''
    def __init__(self):
        self.array = []
        self.sortedArray = SortedArray()

    def push(self, x):
        self.array.append(x)
        self.sortedArray.push((x, len(self.array)))

    def pop(self):
        self.sortedArray.remove((self.array[-1], len(self.array)))
        self.array.pop()

    def top(self):
        return self.array[-1]

    def getMin(self):
        return self.sortedArray.min()[0]


class MinStack(object):
    '''算法思路：

    用一个 stack, 维护一个最小指针，pop 的时候最坏为 O(n)，不过 push 的时候始终为O(1)

    结果：AC
    '''
    def __init__(self):
        self.array = []
        self.min = 0

    def push(self, x):
        '''O(1)'''

        self.array.append(x)
        if self.array[-1] < self.array[self.min]:
            self.min = len(self.array) - 1

    def pop(self):
        '''最坏 O(n)'''

        self.array.pop()
        if self.min < len(self.array):
            return

        self.min = 0
        for i in xrange(len(self.array)):
            if self.array[i] < self.array[self.min]:
                self.min = i

    def top(self):
        return self.array[-1]

    def getMin(self):
        return self.array[self.min]


class MinStack(object):
    '''算法思路：

    维护一个最小值的数组，这样做的依据是栈的每个状态的最小值是固定的，因此只要把每个
    状态的最小值保存起来就可以了

    各个操作均为 O(1)

    结果：AC
    '''
    def __init__(self):
        self.array = []
        self.mins = []

    def push(self, x):
        self.array.append(x)

        if not self.mins:
            self.mins.append(x)
            return

        self.mins.append(min(x, self.mins[-1]))

    def pop(self):
        self.array.pop()
        self.mins.pop()

    def top(self):
        return self.array[-1]

    def getMin(self):
        return self.mins[-1]


class MinStack(object):
    '''算法思路：

    依据同上，不过只用了一个数组

    结果：AC
    '''
    def __init__(self):
        self.array = []

    def push(self, x):
        self.array.append([x, min(x, self.array[-1][1]) if self.array else x])

    def pop(self):
        self.array.pop()

    def top(self):
        return self.array[-1][0]

    def getMin(self):
        return self.array[-1][1]


stack = MinStack()
stack.push(0)
stack.push(1)
stack.push(0)

print stack.getMin()
stack.pop()
print stack.getMin()
