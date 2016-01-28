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

    算出两个 list 的长度的 diff，longer 开始的前 diff 不比较，比较剩下的
    '''
    def getIntersectionNode(self, headA, headB):
        a, b, i, diff, longer, shorter = headA, headB, 0, 0, headA, headB
        while a or b:
            if not a or not b:
                h = a or b

                if h == b:
                    longer, shorter = headB, headA

                while h:
                    diff += 1
                    h = h.next

                break

            a, b = a.next, b.next

        while longer:
            i += 1

            if i > diff:
                if longer == shorter:
                    return longer
                shorter = shorter.next

            longer = longer.next


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
