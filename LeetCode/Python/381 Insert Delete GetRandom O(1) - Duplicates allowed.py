# -*- coding: utf-8 -*-

"""
Insert Delete GetRandom O(1) - Duplicates allowed
=================================================

Design a data structure that supports all following operations in average
O(1) time.

Note: Duplicate elements are allowed.

    insert(val): Inserts an item val to the collection.
    remove(val): Removes an item val from the collection if present.
    getRandom: Returns a random element from current collection of elements.
               The probability of each element being returned is linearly
               related to the number of same value the collection contains.

Example:

    // Init an empty collection.
    RandomizedCollection collection = new RandomizedCollection();

    // Inserts 1 to the collection. Returns true as the collection did not
    // contain 1.
    collection.insert(1);

    // Inserts another 1 to the collection. Returns false as the collection
    // contained 1. Collection now contains [1,1].
    collection.insert(1);

    // Inserts 2 to the collection, returns true. Collection now contains
    // [1,1,2].
    collection.insert(2);

    // getRandom should return 1 with the probability 2/3, and returns 2 with
    // the probability 1/3.
    collection.getRandom();

    // Removes 1 from the collection, returns true. Collection now contains
    // [1,2].
    collection.remove(1);

    // getRandom should return 1 and 2 both equally likely.
    collection.getRandom();
"""

import collections
import random


class RandomizedCollection(object):
    """算法思路：

    同I，只不过是record里边每一个元素的值是一个集合。
    """
    def __init__(self):
        self.queue = []
        self.record = collections.defaultdict(set)

    def insert(self, val):
        r = val not in self.record

        self.queue.append(val)
        self.record[val].add(len(self.queue) - 1)

        return r

    def remove(self, val):
        if val not in self.record:
            return False

        pos = self.record[val].pop()
        if not self.record[val]:
            self.record.pop(val)

        if pos != len(self.queue) - 1:
            self.queue[pos] = self.queue[-1]
            self.record[self.queue[-1]].discard(len(self.queue) - 1)
            self.record[self.queue[-1]].add(pos)

        self.queue.pop()

        return True

    def getRandom(self):
        return random.choice(self.queue)
