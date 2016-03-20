# -*- coding: utf-8 -*-

'''
Intersection of Two Linked Lists
================================

Write a program to find the node at which the intersection of two singly linked
lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function
  returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<ListNode {}>'.format(self.val)


class Solution(object):
    '''算法思路：

    算出两个 list 的长度的 diff，前 diff 个不比较，比较剩下的
    '''
    def cout(self, head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt

    def getIntersectionNode(self, headA, headB):
        l1, l2, cnt1, cnt2 = headA, headB, self.cout(headA), self.cout(headB)
        if cnt2 > cnt1:
            l1, l2 = l2, l1

        for _ in range(abs(cnt1 - cnt2)):
            l1 = l1.next

        while l1:
            if l1 is l2:
                return l1

            l1, l2 = l1.next, l2.next


a = ListNode(5)
b = ListNode(6)
c = ListNode(7)

d = ListNode(8)
e = ListNode(9)

f = ListNode(10)
g = ListNode(11)
h = ListNode(12)

a.next = b
b.next = c
c.next = f

d.next = e
e.next = f

f.next = g
g.next = h

s = Solution()
print s.getIntersectionNode(a, a)
