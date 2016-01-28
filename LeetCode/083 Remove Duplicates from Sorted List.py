# -*- coding: utf-8 -*-

'''
Remove Duplicates from Sorted List
==================================

Given a sorted linked list, delete all duplicates such that each element appear
only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


class Solution(object):
    '''算法思路：

    找到第一个重复的和第一个不重复的，连接起来即可
    '''
    def deleteDuplicates(self, head):
        pre, current = None, head

        while current:
            if not pre:
                pre = current
            elif pre.val != current.val:
                pre.next = current
                pre = current

            current = current.next

        if pre:
            pre.next = None

        return head
