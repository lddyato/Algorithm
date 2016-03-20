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
    """算法思路：

    每次比较当前节点的值是否与 tail 节点相等
    """
    def deleteDuplicates(self, head):
        dummy = tail = ListNode(None)
        while head:
            if head.val != tail.val:
                tail.next = tail = head
            head = head.next

        tail.next = None
        return dummy.next
