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

    每次翻转 list 的前 k 个，如果不足 k 个，那么将已经翻转过来的再翻转过来
    '''
    def reverse(self, head, k):
        rev, current = None, head
        for _ in range(k):
            if current:
                rev, rev.next, current = current, rev, current.next
            else:
                current, head, rev = rev, rev, None
                while current:
                    rev, rev.next, current = current, rev, current.next
                return rev, head, None
        return rev, head, current

    def reverseKGroup(self, head, k):
        if k < 2:
            return head

        dummy = tail = ListNode(None)
        while head:
            start, end, head = self.reverse(head, k)
            tail.next, tail = start, end

        tail.next = None
        return dummy.next
