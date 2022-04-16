class Solution:
    def calculate(self, s: str) -> int:
        
        operators = {'+','-','*','/'}        
        current_number = 0
        operator = '+'
        stack = []
        res = 0
        
        for i,c in enumerate(s):
            if c.isdigit():
                current_number = current_number* 10 + int(c)
                
            if c =='(':
                stack.append(operator)
                operator = '+'
                
            elif c ==')':
                self.append_result_to_stack(stack, current_number, operator)
                current_number = 0
                
                while stack and stack[-1] not in  operators:
                    current_number +=stack.pop()
                operator = stack.pop()
                
            if c in operators or i == len(s) -1:
                self.append_result_to_stack(stack, current_number, operator)
                operator = c
                current_number = 0
                
        while stack:
            res += stack.pop()
            
        return res
    
    
    def append_result_to_stack(self, stack, current_number, operator):
        if operator == '+':
            stack.append(current_number)
            
        elif operator == '-':
            stack.append(-current_number)
            
        elif operator =='*':
            stack.append(stack.pop()* current_number)
            
        else:
            div_result = stack.pop() /current_number
            if div_result < 0:
                stack.append(math.ceil(div_result))
            else:
                stack.append(math.floor(div_result))