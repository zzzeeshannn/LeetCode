import math
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pointer_1 = 0
        pointer_2 = 0
        min_length = math.inf
        min_string = ''
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        missing = 0
        for i in range(0, len(t)):
            t_dict[t[i]]+=1
            missing+=1
        
        while pointer_2<len(s):
            s_dict[s[pointer_2]]+=1
            if s_dict[s[pointer_2]] <= t_dict[s[pointer_2]]:
                missing-=1
            while missing == 0:
                if pointer_2 - pointer_1 + 1 < min_length:
                    min_length = pointer_2-pointer_1+1
                    min_string=s[pointer_1:pointer_2+1]
                s_dict[s[pointer_1]]-=1
                if s_dict[s[pointer_1]]<t_dict[s[pointer_1]]:
                    missing+=1
                pointer_1+=1
            pointer_2+=1
                    
        return min_string