class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Base case 
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        
        # Variable declaration
        same_set = {}
        output = []
        
        # Sorting based on same letter
        for every_str in strs:
            temp_output = sorted(every_str)
            temp = "".join(temp_output)
            if temp not in same_set.keys():
                same_set[temp] = [every_str]
            else:
                same_set[temp].append(every_str)
        
        # Adding the sorted strings to the output
        for key, every_value in same_set.items():
            output.append(every_value)
        
        return output