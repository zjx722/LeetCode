class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        new_arr = [0]*len(nums1)
        
        i, j, k = 0, 0, 0 
        while k< m+n:
            if i<m and j<n and nums1[i] <= nums2[j]:
                new_arr[k] = nums1[i]
                i+=1
            
            elif i<m and j<n and nums1[i] > nums2[j]:
                new_arr[k] = nums2[j]
                j +=1
                
            elif i< m and j>=n:
                new_arr[k] = nums1[i]
                i+=1
                
            else:
                new_arr[k] = nums2[j]
                j +=1
                
                
                
            k+=1
            
        for i in range(len(nums1)):
            nums1[i] = new_arr[i]

        