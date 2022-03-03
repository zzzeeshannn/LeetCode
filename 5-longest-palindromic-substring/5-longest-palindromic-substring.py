class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Required variables 
        longest_substring = ""
        
        # Initialise the DP matrix 
        dp = [[0]*len(s) for _ in range(len(s))]
        
        # Base Case 1
        for i in range(len(s)):
            dp[i][i] = True 
            longest_substring = s[i]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if(s[i] == s[j]):
                    if (j-i == 1) or dp[i+1][j-1]:
                        dp[i][j] = True
                        if(len(longest_substring) < j - i + 1):
                            longest_substring = s[i:j+1]
        
        return longest_substring