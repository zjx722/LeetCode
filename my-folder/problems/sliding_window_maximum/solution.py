class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        
        bigger = deque()
        
        for i, n in enumerate(nums):
            
            while bigger and nums[bigger[-1]] <= n:
                
                bigger.pop()
                
            bigger +=[i]
            
            if i - bigger[0] >= k:
                bigger.popleft()
                
            if i+1 >= k:
                res.append(nums[bigger[0]])
                
        return res
            
            
            
            
        
        
        
        
        