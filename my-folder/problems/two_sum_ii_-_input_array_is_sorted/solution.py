class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hash_map = {}
        
        for index, value in enumerate(numbers):
            rest = target  - value
            
            if rest in hash_map:
                return [ hash_map[rest]+1,index+1]
            
            else:
                hash_map[value] = index
                
        