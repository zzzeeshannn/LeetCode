class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case 
        if (len(strs) == 0):
            return ""
        
        # This is function used later (in Binary Search)
        def checkPrefix(strs: List[str], index: int) -> bool:
            # This function checks if the strings until the passed the index are same
            # We use the first string to extract the prefix, you can choose any :p 
            prefix = strs[0][:index]
            for i in range(1, len(strs)):
                # Here we wanna check that the prefix is in the string and the string --
                # -- starts with the prefix
                if not strs[i].startswith(prefix):
                    return False
            
            return True 
        
        # Variable declaration 
        totalStrings = len(strs)
        lowPtr = 1
        highPtr = min(len(strs[i]) for i in range(totalStrings))
        
        # Base case 
        if(totalStrings == 1):
            # There is only 1 string in the list 
            # So the longest common prefix is the string itself
            return strs[0]
        
        # Setting up binary search 
        # Aim of this binary search is to get the length of the substring --
        # -- which is common got all strings. This will eventually br our longest common prefix 
        while lowPtr <= highPtr: 
            # Get the index
            midPtr = lowPtr + (highPtr - lowPtr) // 2
            
            # If the selected substring is common in all strings
            if (checkPrefix(strs, midPtr)): 
                # This means that we found a common prefix
                # But we want to see if we can find a longer prefix 
                # So, we keep increasing the length 
                lowPtr = midPtr + 1
            else:
                # This means this is not a common prefix in all the strings and we wanna --
                # -- reduce the length and check if we can find one 
                highPtr = midPtr - 1
        
        # We return the prefix
        # From the binary search, we have the index
        # So we pick up any string from the list till that index --
        # -- and that'll be our longest common prefix
        
        return strs[0][:(lowPtr+highPtr)//2]