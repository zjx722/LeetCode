class Solution:
    def calculate(self, s: str) -> int:
        
        if not s:
            return "0"
        
        stack,number,sign = [],0,"+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                number = number*10 + int(s[i])
                                
            if (not s[i].isdigit() and not s[i].isspace()) or i== len(s)-1:
                
                if sign =="-":
                    stack.append(-number)
                elif sign =="+":
                    stack.append(number)                  
                elif sign =="*":
                    stack.append(stack.pop()* number)                    
                else:
                    tmp = stack.pop()
                    if tmp <0 and tmp%number !=0:
                        stack.append(tmp//number +1)
                    else:
                        stack.append(tmp//number)
                                
                number = 0 
                sign = s[i]
            
            
        return sum(stack)
            
        
                    
                    

 
                
                
                
                
            
        
        