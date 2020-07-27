#encoding=utf-8
import itertools
class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        res = 0
        for triangle in itertools.combinations(points, 3):
            res =  max(res, area(*triangle)

        return res