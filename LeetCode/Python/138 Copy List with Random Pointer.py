# -*- coding: utf-8 -*-

'''
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


class Solution(object):
    '''算法思路：

    第一遍利用 hash 建立 {label: node} 的映射
    第二遍将 node 中的 random 补充完整
    '''
    def copyRandomList(self, head):
        record = {}
        newHead = tail = None

        current = head
        while current:
            node = RandomListNode(current.label)

            if tail is None:
                newHead = node
            else:
                tail.next = node

            record[current.label] = tail = node
            current = current.next

        while head:
            if head.random:
                record[head.label].random = record[head.random.label]
            head = head.next

        return newHead
