class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        item_list = [key for key in counter if counter[key] == 1]
        for i, val in enumerate(s):
            if val in item_list:
                return i
        
        return -1