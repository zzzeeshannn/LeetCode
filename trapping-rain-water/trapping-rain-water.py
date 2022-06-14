class Solution:
    def trap(self, height: List[int]) -> int:
        # Variable declaration 
        i = 0 
        j = len(height) - 1
        lowest = 0
        highest = 0
        left = [0]*len(height)
        right = [0]*len(height)
        output = 0
        itr = 0
        
        while i < len(height):
            if i == 0:
                left[i] = height[i]
            else:
                left[i] = max(left[i-1], height[i])
            i += 1
        
        while j > 0:
            if j == len(height)-1:
                right[j] = height[j]
            else:
                right[j] = max(right[j+1], height[j])
            j -= 1
        
        while itr < len(height)-1:
            if itr == 0 or itr == len(height)-1:
                output += 0
            else:
                output += max(0, min(left[itr], right[itr])-height[itr])
            itr += 1
        
        return output
        