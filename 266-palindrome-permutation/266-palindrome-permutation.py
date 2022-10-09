class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Variable declaration 
        oddCount = 0
        if (len(s)%2 == 0): 
            isEven = True
        else: 
            isEven = False
        
        countList = [count for char, count in Counter(s).items()]
        countList = sorted(countList)
        
        for every_count in countList: 
            if every_count % 2 != 0: 
                oddCount += 1
        
        if isEven and oddCount > 0:
            return False 
        if not isEven and oddCount > 1: 
            return False
        
        return True