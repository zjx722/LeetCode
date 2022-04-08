class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        count = 0
        
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':                
                    self.isIsland(grid, i,j)
                    count +=1
        
        return count
                
    def isIsland(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return
            
        grid[row][col] = 'visited'

        self.isIsland(grid, row -1, col)
        self.isIsland(grid, row +1, col)
        self.isIsland(grid, row, col -1)
        self.isIsland(grid, row, col +1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        