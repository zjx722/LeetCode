class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        
        self.board = board
        
        for i in range(len(board)):
            for j in range(len(board[0])):           
                if self.next(i,j,word):
                    return True

                    
        return False
                    
                    
    def next(self, i,j, suffix):
        
        if len(suffix) ==0 :
            return True
        if i < 0 or j < 0 or i>= len(self.board) or j >= len(self.board[0]) or suffix[0] != self.board[i][j]:
            return False 
          
        ret = False
        self.board[i][j] = '*'
            
            
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret  = self.next(i+rowOffset,j + colOffset,suffix[1:])            
            if ret: break
            
        self.board[i][j] = suffix[0]
        
        return ret
                
        