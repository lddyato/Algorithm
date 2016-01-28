# -*- coding: utf-8 -*-

'''
Remove Linked List Elements
===========================

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''


class Solution(object):
    '''算法思路：

    找到要移除的 node 的前一个 pre，并把 pre.next 置为 node 的下一个不为 val 的 node
    '''
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        current, pre, flag = head, None, False
        while current:
            if current.val == val:
                flag = True
            else:
                if flag:
                    pre.next = current
                    flag = False

                pre = current

            current = current.next

        if flag:
            pre.next = None

        return head
