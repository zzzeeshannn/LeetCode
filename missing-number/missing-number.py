class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Variable declaration 
        n = len(nums)
        expected_sum = int(n*(n+1)/2)
        total_sum = 0
        
        for every_num in nums:
            total_sum += every_num
        
        if total_sum == expected_sum:
            return 0 
        else:
            return expected_sum - total_sum