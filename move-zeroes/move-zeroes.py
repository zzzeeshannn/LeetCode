class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Variable declarations
        low = 0
        
        if(len(nums) == 0 or len(nums) == 1):
            return nums
        
        while True and low <= len(nums)-1:
            if(nums[low] == 0):
                break 
            else:
                low += 1
        
        if(low == len(nums)-1):
            return nums 
        else:
            high = low + 1
        
        while high <= len(nums)-1:
            if(nums[high] != 0):
                nums[low] = nums[high]
                high += 1
                low += 1
            else:
                high += 1
        
        
        while low <= len(nums)-1:
            nums[low] = 0
            low += 1
        
        return nums