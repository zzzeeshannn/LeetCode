class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        if(len(nums) == 0):
            return -1
        while low <= high:
            mid = low + (high - low)//2
            if(nums[mid] == target):
                return mid 
            elif(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        
        return -1