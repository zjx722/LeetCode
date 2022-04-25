class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = defaultdict(list)
        
        for index,n in enumerate(nums):
            if dic[n]:
                prev = dic[n][-1]
                if index -prev <= k:
                    return True
                    
            dic[n].append(index)
            
        return False
            
            
            
            
        