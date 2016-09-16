# -*- coding: utf-8 -*-

'''
Course Schedule II
==================

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If
it is impossible to finish all courses, return an empty array.

For example:

    2, [[1,0]]

There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So the correct course order is [0,1]

    4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take. To take course 3 you should have
finished both courses 1 and 2. Both courses 1 and 2 should be taken after you
finished course 0. So one correct course order is [0,1,2,3]. Another correct
ordering is[0,2,1,3].

Note:
- The input prerequisites is a graph represented by a list of edges, not
  adjacency matrices. Read more about how a graph is represented.
'''


import collections


class Solution(object):
    '''算法思路：

    拓扑排序，kahn 算法
    '''
    def findOrder(self, numCourses, prerequisites):
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        v = {i: 0 for i in xrange(numCourses)}

        for to, from_ in prerequisites:
            graph[from_][to] += 1
            v[to] += 1

        path = []
        queue = collections.deque([key for key, val in v.items() if val == 0])
        while queue:
            vertex = queue.popleft()
            path.append(vertex)

            for to in graph[vertex]:
                v[to] -= graph[vertex][to]
                if v[to] == 0:
                    queue.append(to)

            del graph[vertex]

        return [] if graph else path


s = Solution()
print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
