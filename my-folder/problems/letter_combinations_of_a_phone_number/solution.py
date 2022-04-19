class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
        if not digits:
            return []
        
        res = []
        
        self.backtrack(res,'',digits)
        
        return res
        
    def backtrack(self,res, curr_str, digits):
        if len(digits) == 0:
            return res.append(curr_str)
        
        mapping = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        
        for char in mapping[digits[0]]:
            self.backtrack(res, curr_str + char, digits[1:])
            
    
            
        