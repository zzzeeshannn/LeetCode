class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        res = 0
        for i,c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())
        return res