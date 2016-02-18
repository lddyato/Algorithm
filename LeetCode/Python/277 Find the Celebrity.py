# -*- coding: utf-8 -*-

'''
Find the Celebrity
==================

Suppose you are at a party with n people (labeled from 0 to n - 1) and among
them, there may exist one celebrity. The definition of a celebrity is that all
the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you
know B?" to get information of whether A knows B. You need to find out the
celebrity (or verify there is not one) by asking as few questions as possible
(in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A
knows B. Implement a function int findCelebrity(n), your function should
minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the
celebrity's label if there is a celebrity in the party. If there is no
celebrity, return -1.
'''


class Solution(object):
    '''算法思路：

    维护一个有可能为 Celebrity 的集合，每次用排除法筛掉不可能为 Celebrity 的元素
    '''
    def getKnows(self, a, b):
        key = '{}:{}'.format(a, b)
        if key not in self.record:
            self.record[key] = knows(a, b)
        return self.record[key]

    def findCelebrity(self, n):
        possible, p, self.record = dict(enumerate(xrange(n))), None, {}
        while possible:
            p = possible.keys()[0] if p is None else p
            for i in xrange(n):
                if i == p:
                    continue

                if self.getKnows(p, i) or not self.getKnows(i, p):
                    del possible[p]
                    p = i if i in possible else None
                    break
            else:
                return p

        return -1
