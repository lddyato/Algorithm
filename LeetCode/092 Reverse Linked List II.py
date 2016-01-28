# -*- coding: utf-8 -*-

'''
Reverse Linked List II
======================

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    遍历一次，从 m 处开始反转，在 n 处停止反转，要注意的地方：
      - 反转序列 与前后的衔接
      - 新的序列 head 的获取
    '''
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        i, current = 1, head
        start_pre = start = pre = next = new_head = None

        while current:
            next = current.next

            if i + 1 == m:
                start_pre = current

            elif m <= i <= n:
                if i == m:
                    start = current
                elif i == n:
                    if start_pre:
                        start_pre.next = current
                        new_head = head
                    else:
                        new_head = current

                    start.next = current.next

                current.next = pre

            pre = current
            current = next

            i += 1

        return new_head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
head = s.reverseBetween(a, 2, 4)

while head:
    print head
    head = head.next
