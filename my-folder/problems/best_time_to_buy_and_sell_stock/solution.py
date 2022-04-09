class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        slow, fast = 0,0
        
        
        while fast < len(prices):
            cur = prices[fast] - prices[slow]           
            max_p = max(cur,max_p)
            
            if prices[fast] < prices[slow]:
                slow = fast
            fast +=1
                
        return max_p
                

        