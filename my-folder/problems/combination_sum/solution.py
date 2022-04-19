class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        self.backtrack(res, [], candidates, target)
                
        return res
    
    def backtrack(self, res, curr_arr, candidates, target):
    
        if target ==0 :
            res.append(curr_arr)
            return
        
        elif target <0:
            return
        
        else:
            for i in range(len(candidates)):
                self.backtrack(res, curr_arr+[candidates[i]], candidates[i:],target- candidates[i])
        