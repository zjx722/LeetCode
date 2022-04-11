class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        if len(s) %2 ==1:
            return False
        
        i = 0
        while  i < len(s):
            if s[i] in "{[(":
                stack.append(s[i])
                
            elif s[i] ==')':
                if not stack:
                    return False                
                c = stack.pop() 
                if c != '(':
                    return False

                    
            elif s[i] ==']':
                if not stack:
                    return False                
                c = stack.pop() 
                if c != '[':
                    return False

                    
            elif s[i] =='}':
                if not stack:
                    return False                
                c = stack.pop() 
                if c != '{':
                    return False
                    
            i +=1
                    
        return not stack
                
                    
            
        
        
        