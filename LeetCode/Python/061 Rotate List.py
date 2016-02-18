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
    def rotateRight(self, head, k):
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1

        if not n or not k % n:
            return head

        tail, k = head, k % n
        for _ in xrange(n - k - 1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head
        return next
