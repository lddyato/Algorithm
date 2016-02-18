# -*- coding: utf-8 -*-

'''
Remove Duplicates from Sorted List II
=====================================

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''


class Solution(object):
    '''算法思路：

    找到前后 node 不一样的 node，然后连接起来
    '''
    def deleteDuplicates(self, head):
        new_head, tail, pre, current = None, None, None, head
        while current:
            if (pre is None or pre.val != current.val) and (
                    current.next is None or current.next.val != current.val):
                if not new_head:
                    new_head = tail = current
                else:
                    tail.next = current
                    tail = current

            pre, current = current, current.next

        if tail:
            tail.next = None

        return new_head
