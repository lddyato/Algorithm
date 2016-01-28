# -*- coding: utf-8 -*-

'''
Rotate List
===========

Given a list, rotate the list to the right by k places, where k is
non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


class Solution(object):
    '''算法思路：

    快慢指针的变形，等过了 n 步慢指针才开始跑

    本题的一个坑是：如果 k > length of list，结果不是不翻转，而是以 k = k % length
    的方式去取结果

    临界条件：
    - k = 0
    - k = length of list
    - k > length of list
    - list 为空
    '''
    def get_k(self, head, k):
        length, current = 0, head
        while current:
            length += 1
            current = current.next

        return length and k % length or k

    def rotateRight(self, head, k):
        k = self.get_k(head, k)

        n, pre, pivot, current, tail = 0, None, None, head, None
        while current:
            n += 1

            if k and n - k >= 0:
                pre, pivot = pivot, pivot and pivot.next or head

            if not current.next:
                tail = current

            current = current.next

        if pre:
            pre.next = None
            tail.next = head

        return pivot or head
