class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)
        
        for word in strings:
            
            order_list = [0]
            prev = word[0]
            
            if len(word) >1:
                for char in word[1:]:
                    diff = ord(char)-ord(prev)
                    if diff < 0:
                        diff += 26
                        
                    order_list.append(diff)
                    prev = char
                        
            mapping[tuple(order_list)].append(word)
            
        return mapping.values()
        
        