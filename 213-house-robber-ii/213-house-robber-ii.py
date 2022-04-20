class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) ==1: 
            return nums[0]
        
        return max(self.simple_rob(nums[1:]), self.simple_rob(nums[:-1]))
    
    def simple_rob(self, nums):
        
        dp_l1, dp_l2 = 0,0
        
        dp = 0
        
        for n in nums:
            dp_l1 = dp
            dp = max(dp_l1, dp_l2+ n )
            
            dp_l2 = dp_l1
            
        return dp
        
            
            
            
            
        