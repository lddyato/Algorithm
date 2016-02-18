# -*- coding: utf-8 -*-

'''
Swap Nodes in Pairs
===================

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    遍历一边，当是偶数的时候，交换和前边的 node

    需要注意的是: 一般遍历下个节点是 current = current.next，但是这里 current.next
    被赋值为 pre，因此为 current = next
    '''
    def swapPairs(self, head):
        n, new_head, last, pre, current = 1, None, None, None, head
        while current:
            next = current.next

            if n & 1:
                pre = current
            else:
                current.next = pre
                pre.next = next

                if last:
                    last.next = current

                last = pre
                new_head = new_head or current

            current = next

            n += 1

        return new_head or head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

s = Solution()
print s.swapPairs(a)
