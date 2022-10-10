class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for every_num in nums: 
            if (len(str(every_num)) % 2 == 0):
                count += 1
        
        return count