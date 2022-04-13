class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        hold = [0]* (len(prices)+1)
        sold = [0]* (len(prices)+1)
        
        hold[0] = float(-inf)
        sold[0] = 0
        
        for i in range(1, len(prices)+1):
            hold[i] = max(hold[i-1],sold[i-1]- prices[i-1] -fee)
            
            sold[i] = max(sold[i-1],hold[i-1]+ prices[i-1])
            
        
        return sold[-1]