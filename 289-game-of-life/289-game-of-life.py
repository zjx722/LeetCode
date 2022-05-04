class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
#         current_board =[[0] *len(board[0])] * len(board)
        
        
#         i= 0
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 current_board[i][j] = board[i][j]
                
                
        current_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
                
        neighbor = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1),(-1,1),(1,-1)]   
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                live = 0
                for  value in neighbor:
                    i,j = value[0],value[1]
                    if row+i >=0 and row+i<len(board) and col+j >=0 and col+j <len(board[0]):
                        live += current_board[row+i][col+j]
                if current_board[row][col] == 1:
                    if live <2 or live >3:
                        board[row][col] = 0
                    elif live ==2 or live==3:
                        board[row][col] = 1
                        
                else:
                    if live ==3:
                        board[row][col] = 1
                        
        
                    
                