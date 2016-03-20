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

    每次比较当前节点值与 val 是否相等，如果不相等则把他 append 列表结尾
    '''
    def removeElements(self, head, val):
        dummy = tail = ListNode(None)
        while head:
            if head.val != val:
                tail.next = tail = head
            head = head.next

        tail.next = None
        return dummy.next