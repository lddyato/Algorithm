# -*- coding: utf-8 -*-

"""
Insert Delete GetRandom O(1)
===========================

Design a data structure that supports all following operations in average
O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each
           element must have the same probability of being returned.

Example:

    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();

    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);

    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);

    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);

    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();

    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);

    // 2 was already in the set, so return false.
    randomSet.insert(2);

    // Since 1 is the only number in the set, getRandom always return 1.
    randomSet.getRandom();
"""

import random


class RandomizedSet(object):
    """算法思路：

    维护一个序列，和一个{num: index}的哈希表。

    insert：append到序列末尾，然后在哈希表里边记录该数的index
    remove：不能直接在数组中删除该数，因为这样的效率复杂度为O(n)，但是我们知道
            pop数组中最后一个数的复杂度为O(n)，这样我们可以先把最后一个数放到
            要删除的数的位置上，然后再把最后一个数删除，这样复杂度就变成了O(1)。
    """
    def __init__(self):
        self.record = {}
        self.queue = []

    def insert(self, val):
        if val in self.record:
            return False

        self.queue.append(val)
        self.record[val] = len(self.queue) - 1
        return True

    def remove(self, val):
        if val not in self.record:
            return False

        self.queue[self.record[val]] = self.queue[-1]
        self.record[self.queue[-1]] = self.record[val]

        self.queue.pop()
        self.record.pop(val)
        return True

    def getRandom(self):
        return random.choice(self.queue)
