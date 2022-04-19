class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
               
        left,right = [1],[1]
        
        for i in range(1,len(nums)):            
            product = left[-1]*nums[i-1]
            left.append(product)
            
        for i in range(len(nums)-2,-1,-1):
            product = right[-1]* nums[i+1]           
            right.append(product)
            
        right.reverse()
        res = []
        
        for i in range(len(nums)):
            res.append(left[i]*right[i])
               
        return res
            
        
