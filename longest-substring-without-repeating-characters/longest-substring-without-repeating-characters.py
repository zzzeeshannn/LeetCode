class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable declaration 
        char = [0] * 128 
        left = 0
        right = 0
        res = 0 
        
        while right < len(s):
            char[ord(s[right])] += 1
            while char[ord(s[right])] > 1:
                char[ord(s[left])] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        
        return res