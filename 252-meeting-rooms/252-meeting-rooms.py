class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_times = sorted(intervals)
        for i in range(len(sorted_times)): 
            if i < len(sorted_times)-1: 
                if sorted_times[i][1] > sorted_times[i+1][0]:
                    return False 
        
        return True