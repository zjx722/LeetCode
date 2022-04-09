class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <=1:
            return 0
        
        fast, prev_fast = 0, 0
        res = 0
        
        while fast < len(prices) :
            if prices[fast] > prices[prev_fast] :
                
                res += prices[fast] - prices[prev_fast]

            prev_fast = fast            
            fast +=1
            

            
        return res
                
                