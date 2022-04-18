class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []       
        self.backtracking(res, '', 0,0,n)
               
        return res
        
        
    def backtracking(self,res, current_str,left,right,n):
        if 2*n  == len(current_str)  :
            res.append(current_str)
            return 
        
        if left < n: 
            self.backtracking(res, current_str +'(', left+1, right, n)
        if left> right:
            self.backtracking(res, current_str + ')', left, right+1,n)