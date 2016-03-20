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

    每走一步判断当前节点是否应该被添加到列表里边
    '''
    def deleteDuplicates(self, head):
        dummy = tail = ListNode(None)
        while head:
            node = head
            if head.next and head.next.val == node.val:
                while head and head.val == node.val:
                    head = head.next
            else:
                tail.next, tail, head = head, head, head.next

        tail.next = None
        return dummy.next
