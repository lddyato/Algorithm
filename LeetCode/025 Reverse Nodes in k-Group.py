# -*- coding: utf-8 -*-

'''
Reverse Nodes in k-Group
========================

Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end
should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''


class Solution(object):
    '''算法思路：

    数到 k 的倍数时反转
    '''
    def reverseKGroup(self, head, k):
        if k < 2:
            return head

        n, new_head, last, start, current = 0, None, None, None, head
        while current:
            n += 1

            next = current.next

            if n % k:
                start = start or current
            else:
                rev, cursor = None, start
                while cursor != next:
                    rev, rev.next, cursor = cursor, rev, cursor.next

                start.next = next

                if last:
                    last.next = rev

                last = start
                start = None

                new_head = new_head or rev

            current = next

        return new_head or head
