class Solution:
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        while L < R:
            if height[L] < height[R]:
                res, L = max(res, height[L] * (R - L )), L + 1
            else:
                res, R = max(res, height[R] * (R - L )), R - 1
        return res