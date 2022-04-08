class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        
        for index, n in enumerate(nums):
            rest = target - n
            if rest in index_map:
                return [index_map[rest], index]
            else:
                index_map[n] = index
        