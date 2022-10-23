class Solution:
    def firstUniqChar(self, s: str) -> int:
        character_list = [char for char, value in Counter(s).items() if value == 1]
        
        for index, every_char in enumerate(s): 
            if every_char in character_list:
                return index
        
        return -1