# -*- coding: utf-8 -*-

'''
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''


class Solution(object):
    '''算法思路：

    第一遍利用 hash 建立 {old_node: new_node} 的映射
    第二遍将 new_node 中的 random 补充完整
    '''
    def copyRandomList(self, head):
        new_head, tail, current, record = None, None, head, {}
        while current:
            node = record.setdefault(current, RandomListNode(current.label))

            if not new_head:
                new_head = tail = node
            else:
                tail.next = node
                tail = node

            current = current.next

        current, new_current = head, new_head
        while current:
            random = current.random
            if random:
                new_current.random = record[random]

            current, new_current = current.next, new_current.next

        return new_head
