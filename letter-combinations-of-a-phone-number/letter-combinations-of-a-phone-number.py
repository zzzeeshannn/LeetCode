class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case
        if(len(digits) == 0):
            return []
        # Approach with backtracking 
        # Defining all letters for possible numbers 
        char_list = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def backtrack(index, path):
            # Base case 
            if (len(path) == len(digits)):
                output.append("".join(path))
                return 
            else:
                possible_characters = char_list[digits[index]]
                for every_character in possible_characters:
                    path.append(every_character)
                    backtrack(index+1, path)
                    path.pop()
        
        # Defining output holder here 
        output = []
        index = 0
        backtrack(index, [])
        return output