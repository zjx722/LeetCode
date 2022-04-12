class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                  
        res = set()
        for index, target in enumerate(nums):
            
            new_nums = nums[0:index] + nums[index+1:]            
            seen = set()
            
            for i, v in enumerate(new_nums):
                rest = - target - v
                
                if rest in seen:
                    res.add(tuple(sorted((target, rest, v))))
                                    
                seen.add(new_nums[i])
        
        return res
                
                
                
        