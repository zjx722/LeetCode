class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        
        if len(nums)>=2:
            dp[1] = max(nums[0],nums[1])
            
        if len(nums)>=3:    
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-2] +nums[i], dp[i-1])
                
        return dp[-1]