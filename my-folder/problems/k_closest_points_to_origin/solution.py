class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = defaultdict()
        
        # for point in points:
        #     arr[point] = point[0]**2 + point[1]**2 
            
        return sorted(points, key=lambda x: x[0]**2 +x[1]**2 )[:k]
            
