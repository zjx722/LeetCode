class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len ==0:
            return 0
        
        new_list = []
        
        p1,p2 = 0, 0
        
        while len(new_list) < total_len//2 +1:
        
            if  p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    new_list.append(nums1[p1])
                    p1 +=1

                else:
                    new_list.append(nums2[p2])
                    p2 +=1 
                    
            elif p1 < len(nums1):
                new_list.append(nums1[p1])
                p1 +=1
            else:
                new_list.append(nums2[p2])
                p2+=1
                
        
            
        
        if total_len % 2 ==1:
            return new_list[-1]
        else:
            return (new_list[-1]+new_list[-2])/2
            