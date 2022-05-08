class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        self.backtrack(res,nums,[])
        
        return res
        
        
    def backtrack(self, res, nums, cur):
        
        if not nums:
            res.append(cur)
            #return
                      
        for i in range(len(nums)):
            

            self.backtrack(res,nums[:i] +nums[i+1:],cur + [nums[i]])



        