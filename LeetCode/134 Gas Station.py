# -*- coding: utf-8 -*-

'''
Gas Station
===========

There are N gas stations along a circular route, where the amount of gas at
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit
once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''


class Solution(object):
    '''算法思路：

    所有的情况都遍历

    结果：TLE
    '''
    def canCompleteCircuit(self, gas, cost):
        for start in xrange(len(gas)):
            i = s = s_cost = 0

            while i < len(gas):
                p = (start + i) % len(gas)

                s += gas[p]
                s_cost += cost[p]

                if s_cost > s:
                    break

                i += 1
            else:
                return start

        return -1


class Solution(object):
    '''算法思路：

    找出 ∑(gas[i] - cost[i]) 最小的地方，下一站即为结果
    '''
    def canCompleteCircuit(self, gas, cost):
        i, s, p, m = 0, 0, 0, float('inf')
        while i < len(gas):
            s += gas[i] - cost[i]
            if s < m:
                m, p = s, i
            i += 1

        return (p + 1) % len(gas) if s >= 0 else -1


s = Solution()
print s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
print s.canCompleteCircuit([2, 3, 1], [3, 1, 2])
