class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <=1:
            return len(intervals)
        
        
        used_rooms = 0
        
        start_time = sorted([i[0] for i in intervals])
        end_time  = sorted([i[1] for i in intervals])
        
        start, end = 0, 0
        
        while start < len(intervals):
            
            if start_time[start] >= end_time[end]:
                used_rooms -=1
                end +=1
            
            used_rooms +=1
            start +=1
            
        return used_rooms
            
            
        
        