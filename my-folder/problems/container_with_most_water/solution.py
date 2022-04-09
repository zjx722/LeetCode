class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water = 0
        
        left, right = 0, len(height)-1
        
        while left < right:
            
            if height[left] < height[right]:
                current_water = height[left]*(right-left)
                max_water = max(max_water, current_water)
                left +=1
                
            else:
                current_water = height[right]*(right-left)
                max_water = max(max_water, current_water)
                right -=1
                
        return max_water
        