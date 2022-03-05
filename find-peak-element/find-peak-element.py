class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Required parameters 
        low = 0 
        high = len(nums)-1
        
        # Iterative Binary Search
        while low < high: 
            mid = low + (high-low)//2 
            if(nums[mid] < nums[mid+1]):
                low = mid + 1
            else:
                high = mid 
        
        return low