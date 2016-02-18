# -*- coding: utf-8 -*-

'''
Linked List Cycle
=================

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


class Solution(object):
    '''算法思路：

    利用快慢指针，如果快指针追上了慢指针，说明有 cycle
    '''
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        return False
