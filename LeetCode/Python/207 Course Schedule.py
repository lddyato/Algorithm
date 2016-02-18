# -*- coding: utf-8 -*-

'''
Course Schedule
===============

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

    2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

    2, [[1,0],[0,1]]

There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Note:
- The input prerequisites is a graph represented by a list of edges, not
  adjacency matrices. Read more about how a graph is represented.
'''


import collections


class Solution(object):
    '''算法思路：

    可以简化成寻找有向图中是否有环，这里使用 kahn 算法来判断

    需要注意的一点是，prerequisites 可能具有重复的边
    '''
    def canFinish(self, numCourses, prerequisites):
        graph, v = collections.defaultdict(set), [0] * numCourses

        for to, start in prerequisites:
            if to not in graph[start]:
                graph[start].add(to)
                v[to] += 1

        stack = collections.deque(i for i, val in enumerate(v) if not val)
        while stack:
            top = stack.popleft()
            for node in graph[top]:
                v[node] -= 1
                if not v[node]:
                    stack.append(node)
            del graph[top]

        return not bool(graph)


s = Solution()
print s.canFinish(4, [[0,3],[2,0],[2,1],[3,2]])
