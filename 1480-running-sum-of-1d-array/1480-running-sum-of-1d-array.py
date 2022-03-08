class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Variable declaration 
        output = []
        val = 0
        
        for num in nums: 
            val += num 
            output.append(val)
        
        return output