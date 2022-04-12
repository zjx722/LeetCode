class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        shortest = min(strs, key = len)
        
        for i in range(len(shortest)):
            for other in strs:
                if other[i] !=shortest[i]:
                    return shortest[:i]
        
        
                
        return shortest
        