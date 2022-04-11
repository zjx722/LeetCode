class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        fast, curr,res_max = 0,[],0
        
        while fast < len(s):
            
            curr.append(s[fast])
            
            while len(set(curr)) >k:
                curr = curr[1:]
                
            
            res_max = max(res_max, len(curr))
            
            fast +=1
            
        return res_max
        