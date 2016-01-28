# -*- coding: utf-8 -*-

'''
Rectangle Area
==============

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as
shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
'''


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        s = (C - A) * (D - B) + (G - E) * (H - F)
        w, h = (min(C, G) - max(A, E)), (min(D, H) - max(B, F))

        return s - (0 if w <= 0 or h <=0 else w * h)


s = Solution()
print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
