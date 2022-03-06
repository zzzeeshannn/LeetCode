class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = True
        else:
            flag = False
        
        result = ""
        string_val = str(abs(x))
        for i in range(len(string_val)-1, -1, -1):
            result += string_val[i]
        
        output = int(result)
        
        if flag:
            output = 0 - output
        
        if output >= pow(2, 31) or output < -pow(2, 31):
            return 0
        return output
            