class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        substring_length = len(part)
        while part in s:
            substring_index = s.find(part)
            right_index = substring_index + substring_length
            
            left_substring = s[:substring_index]
            right_substring = s[right_index:]
            s = left_substring + right_substring 
        
        return s