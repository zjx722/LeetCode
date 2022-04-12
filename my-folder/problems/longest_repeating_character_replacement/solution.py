class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        fast, slow = 0, 0         
        maxf = 0         
        counter = collections.Counter()     
        res = 0
        
        for fast in range(len(s)):
            
            counter[s[fast]] +=1
            
            maxf = max(maxf, counter[s[fast]])
            
            while fast - slow + 1 - maxf > k:
                
                counter[s[slow]] -=1
                slow +=1
                
            res = max(res, fast - slow +1)
                
                
        return res
                
                