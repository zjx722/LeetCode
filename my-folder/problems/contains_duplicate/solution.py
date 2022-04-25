class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        
        for key, value in dic.items():
            if value >= 2:
                return True
            
        return  False