class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
            
        mid = len(nums)//2 
        
        for mid in range(1,len(nums)-1):
            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid
        
        if nums[0] > nums[-1]:
            return 0
        else:
            return len(nums)-1
                
                
        