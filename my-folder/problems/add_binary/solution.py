class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry,i,j = 0, len(a) -1, len(b)-1
        
        res = []
        
        while i >=0  or j >=0 or carry:
            v1 = 0
            v2 = 0
            
            if i>=0:
                v1 = int(a[i])
                i -=1
            
            if j >=0:
                v2 = int(b[j])
                j -=1
                
            carry, val = divmod(v1+v2+carry, 2)
            
            res.append(str(val))
            
        return ''.join(res[::-1])
            
                
            
            
            
        