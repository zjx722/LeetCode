class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res_max, cur_max,fast = nums[0],nums[0],1
        
        while fast < len(nums):
            cur_max = max(nums[fast],cur_max+nums[fast])
            res_max = max(res_max, cur_max)
           
            fast +=1
            
        return res_max
        