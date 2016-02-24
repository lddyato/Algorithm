# -*- coding: utf-8 -*-

'''
Smallest Rectangle Enclosing Black Pixels
=========================================

An image is represented by a binary matrix with 0 as a white pixel and 1 as a
black pixel. The black pixels are connected, i.e., there is only one black
region. Pixels are connected horizontally and vertically. Given the location
(x, y) of one of the black pixels, return the area of the smallest
(axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]

and x = 0, y = 2,
Return 6.
'''


class Solution(object):
    '''算法思路：

    BFS 遍历找到 左右上下边界

    最坏：O(4*m*n)

    结果：TLE
    '''
    def minArea(self, image, x, y):
        minX, maxX, minY, maxY, m, n = x, x, y, y, len(image), len(image[0])

        queue = [(x, y)]
        for x, y in queue:
            image[x][y] = '2'

            for i, j in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                xx, yy = x + i, y + j
                if 0 <= xx < m and 0 <= yy < n and image[xx][yy] == '1':
                    minX, maxX = min(minX, xx), max(maxX, xx)
                    minY, maxY = min(minY, yy), max(maxY, yy)

                    queue += [(xx, yy)]

        return (maxX - minX + 1) * (maxY - minY + 1)


class Solution(object):
    '''算法思路：

    二分搜索在 row，column 方向上最早和最晚出现的 '1'

    最坏：O(m*log(n) + n*log(m))

    结果：AC
    '''
    def searchLeft(self, image, low, high):
        while low <= high:
            mid = low + high >> 1
            if any(row[mid] == '1' for row in image):
                if mid == 0 or all(row[mid - 1] == '0' for row in image):
                    return mid
                high = mid - 1
            else:
                low = mid + 1

    def searchRight(self, image, low, high, n):
        while low <= high:
            mid = low + high >> 1
            if any(row[mid] == '1' for row in image):
                if mid == n - 1 or all(row[mid + 1] == '0' for row in image):
                    return mid
                low = mid + 1
            else:
                high = mid - 1

    def searchTop(self, image, low, high):
        while low <= high:
            mid = low + high >> 1
            if any(pix == '1' for pix in image[mid]):
                if mid == 0 or all(pix == '0' for pix in image[mid - 1]):
                    return mid
                high = mid - 1
            else:
                low = mid + 1

    def searchBottom(self, image, low, high, m):
        while low <= high:
            mid = low + high >> 1
            if any(pix == '1' for pix in image[mid]):
                if mid == m - 1 or all(pix == '0' for pix in image[mid + 1]):
                    return mid
                low = mid + 1
            else:
                high = mid - 1

    def minArea(self, image, x, y):
        m, n = map(len, (image, image[0]))

        left = self.searchLeft(image, 0, y)
        right = self.searchRight(image, y, n - 1, n)
        top = self.searchTop(image, 0, x)
        bottom = self.searchBottom(image, x, m - 1, m)

        return (right - left + 1) * (bottom - top + 1)


s = Solution()
print s.minArea(['1'], 0, 0)
