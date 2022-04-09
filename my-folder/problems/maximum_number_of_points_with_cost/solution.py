class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n  = len(points), len(points[0])
        if m ==1:
            return max(points[0])
        if n ==1:
            return sum(sum(x) for x in points)
        
        def left(arr):
            lft = [arr[0]] + [0]*(n-1)
            for i in range(1,n):
                lft[i] = max(lft[i-1]-1,arr[i])
                
            return lft
            
        def right(arr):
            rgt = [0]*(n-1) +[arr[-1]]
            for i in range(n-2,-1,-1):
                rgt[i] = max(rgt[i+1]-1, arr[i])
            
            return rgt
        
        
        pre = points[0]
        
        for i in range(m-1):
            lft, rgt, cur = left(pre), right(pre),[0]*n
            for j in range(n):
                cur[j] = points[i+1][j] +max(lft[j],rgt[j])
                
            pre = cur[:]
            
        return max(pre)
        