class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Variable declaration 
        total_product = 1
        flag = 1
        counter = 0
        for every_number in nums: 
            if every_number == 0:
                counter += 1
            else: 
                total_product *= every_number 
        
        if counter > 1:
            for i in range(0, len(nums)):
                nums[i] = 0
        elif counter == 1:
            for i, every_number in enumerate(nums):
                if every_number != 0:
                    nums[i] = 0
                else:
                    nums[i] = total_product
        else:
            for i, every_number in enumerate(nums):
                nums[i] = int(total_product/every_number)
        
        return nums