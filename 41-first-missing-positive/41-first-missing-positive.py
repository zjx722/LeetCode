class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        heap = []
        for n in nums:
            if n>0:
                heapq.heappush(heap, n)
                
        if not heap:
            return 1
        
        count = 1
        while heap:
            value = heapq.heappop(heap)
            if value == count:
                count +=1
            else:
                return count
            
        return value+1
            
                
                
                
        
        
        