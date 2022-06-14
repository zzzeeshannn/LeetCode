class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split_v1 = version1.split(".")
        split_v2 = version2.split(".")
        i = len(split_v1)
        j = len(split_v2)
        
        for itr in range(max(i, j)):
            num1 = int(split_v1[itr]) if itr < i else 0
            num2 = int(split_v2[itr]) if itr < j else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        
        return 0
            