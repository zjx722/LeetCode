class Solution:
    def calculate(self, s: str) -> int:
        
        stack, sign,num = [],1,0
        res = 0
        
        for i in range(len(s)):
            
            if s[i].isdigit():
                
                num  = num*10 + int(s[i])
                
            elif s[i] =="+":
                res += sign * num               
                num = 0
                sign =1
                
            elif s[i] =='-':
                res += sign*num
                num = 0
                sign = -1
                
            elif s[i] =='(':
                stack.append(res)
                stack.append(sign)
                
                sign = 1
                res =0
                
                
                
            elif s[i] ==')':
                res += sign*num
                
                res *= stack.pop()
                
                res += stack.pop()
                
                num = 0
                
        return res + sign*num
                
                
                
                
                
                    
                    
                    
                        
                    
                
        