class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, hold, rest= float('-inf'), float('-inf'), 0
        
        for p in prices:
            
            prev_sold = sold
            
            sold = hold + p
            hold = max(hold,rest-p)
            rest = max(rest, prev_sold)
            
        return max(rest,  sold)   