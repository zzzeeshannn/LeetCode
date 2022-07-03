class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {c: [-1, -1] for c in ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(s) - j) * (j - k)
        return res 
        