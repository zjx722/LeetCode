class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)
        
        for word in strs:
            mapping[tuple(sorted(word))].append(word)
        
        return mapping.values()