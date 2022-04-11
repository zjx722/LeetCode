class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        fast,slow,curr,res_max = 0,0,[],0
        
        while fast < len(s):
            
            curr.append(s[fast])
            
            while len(set(curr)) >2:
                curr = curr[1:]
                slow +=1
            
            res_max = max(res_max, len(curr))
            
            fast +=1
            
        return res_max
            
        