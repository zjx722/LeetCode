class Solution:
    def reverse(self, x: int) -> int:
        
        nums = str(x)
        
        if nums[0] =='-':
            reverse = int(nums[1:][::-1])
            if reverse > 2**31:
                return 0
            else:
                return -1* reverse
        else:
            
            reverse = int(nums[::-1])
            if reverse >2**31-1:
                return 0
            else:
                return reverse