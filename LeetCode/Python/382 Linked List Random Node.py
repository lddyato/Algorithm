# -*- coding: utf-8 -*-

"""
Linked List Random Node
=======================

Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
    What if the linked list is extremely large and its length is unknown to
    you? Could you solve this efficiently without using extra space?

Example:

    // Init a singly linked list [1,2,3].
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    Solution solution = new Solution(head);

    // getRandom() should return either 1, 2, or 3 randomly. Each element
    // should have equal probability of returning.
    solution.getRandom();
"""

import random


class Solution(object):
    """算法思路：

    蓄水池抽样法
    """
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        head, n = self.head, 1

        while head:
            i = random.randint(1, n)
            if i == 1:
                val = head.val

            head = head.next
            n += 1

        return val
