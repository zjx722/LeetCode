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
    
#another#    
# public int maxProfit(int[] prices) {
#         int maxprofit = 0;
#         for (int i = 1; i < prices.length; i++) {
#             if (prices[i] > prices[i - 1])
#                 maxprofit += prices[i] - prices[i - 1];
#         }
#         return maxprofit;
#     }
# }
                
                