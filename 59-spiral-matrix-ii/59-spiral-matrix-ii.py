class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        up, left = 0, 0 
        
        down, right = n-1,n-1
        
        count = 1
        while count <= n*n:
                        
            for col in range(left, right+1):
                matrix[up][col] = count
                count +=1
                             
            for row in range(up+1, down+1):
                matrix[row][right] = count
                count +=1
                
            if up !=  down:                
                for col in range(right-1, left-1, -1):
                    matrix[down][col] = count
                    count +=1
                    
            if right != left:
                for row in range(down-1, up,-1):
                    matrix[row][left] = count
                    count +=1
                    
            up +=1
            down -=1
            left +=1
            right -=1
        
        return matrix