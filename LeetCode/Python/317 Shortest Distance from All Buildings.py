# -*- coding: utf-8 -*-

'''
Shortest Distance from All Buildings My Submissions Question
============================================================

You want to build a house on an empty land which reaches all buildings in the
shortest amount of distance. You can only move up, down, left and right. You
are given a 2D grid of values 0, 1 or 2, where:

- Each 0 marks an empty land which you can pass by freely.
- Each 1 marks a building which you cannot pass through.
- Each 2 marks an obstacle which you cannot pass through.
- For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at
  (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel
distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house
according to the above rules, return -1.
'''


import collections


class Solution(object):
    '''算法思路：

    对于每一个 building 进行 BFS 搜索，如果节点是 0 的话那么就加上从 building 到该节
    点的距离，最后选出距离最小且能够到每个 building的值即可

    这一题第一眼看上去解法过于普通，而且复杂度很高，为 O(m*n*k)，以为不是正解，没想到
    过了，看来有的题目就是考察最基本的知识，没有过多道道
    '''
    def traverse(self, startPoint, m, n, grid, distance, times):
        queue, level, visited = (
            collections.deque([startPoint]), 1, [[0] * n for _ in xrange(m)])

        while queue:
            for _ in xrange(len(queue)):
                i, j = queue.popleft()

                for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    ii, jj = i + x, j + y
                    if (0 <= ii < m and 0 <= jj < n and
                            not (grid[ii][jj] or visited[ii][jj])):
                        queue.append((ii, jj))

                        distance[ii][jj] += level
                        times[ii][jj] += 1
                        visited[ii][jj] = 1
            level += 1

    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])
        distance, times = [[[0] * n for _ in xrange(m)] for _ in xrange(2)]

        buildingNumber = len([
            self.traverse((i, j), m, n, grid, distance, times)
            for i, row in enumerate(grid)
            for j, num in enumerate(row) if num == 1
        ])

        return min([
            distance[i][j]
            for i, row in enumerate(grid)
            for j, num in enumerate(row)
            if not num and times[i][j] == buildingNumber
        ] or [-1])



class Solution(object):
    '''算法思路：

    思路同上，不过可以优化。上述解法用了 distance, times, visited 3 个二维数组，其实
    times 和 visited 是没有必要的，我们只需巧妙的每 BFS 一次，把最开始 0 对应的位置
    -1 即可，而且下次 BFS 搜索的时候，只搜索值为 nth + 1 即可(nth 为当前搜索的第几个
    building 的相反数)，这样就过滤掉了那些不符合要求的分支

    优化前 OJ 大约：1056 ms + 3 x O(mn) Space
    优化后 OJ 大约：104 ms + O(mn) Space
    '''
    def traverse(self, startPoint, m, n, grid, distance):
        queue, level, nth = collections.deque([startPoint]), 1, self.nth

        while queue:
            for _ in xrange(len(queue)):
                i, j = queue.popleft()

                for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    ii, jj = i + x, j + y
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == nth + 1:
                        queue.append((ii, jj))

                        distance[ii][jj] += level
                        grid[ii][jj] = nth
            level += 1

        self.nth -= 1

    def shortestDistance(self, grid):
        m, n, self.nth = len(grid), len(grid[0]), -1
        distance = [[0] * n for _ in xrange(m)]

        buildingNumber = len([
            self.traverse((i, j), m, n, grid, distance)
            for i, row in enumerate(grid)
            for j, num in enumerate(row) if num == 1
        ])

        return min([
            distance[i][j]
            for i, row in enumerate(grid)
            for j, num in enumerate(row)
            if num == -buildingNumber
        ] or [-1])


s = Solution()
print s.shortestDistance([
    [1,0,2,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0]
])
