class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        fast, slow = 0, 0         
        maxf = 0         
        counter = collections.Counter()     
        res = 0
        
        for fast in range(len(answerKey)):
            
            counter[answerKey[fast]] +=1
            
            maxf = max(maxf, counter[answerKey[fast]])
            
            while fast - slow + 1 - maxf > k:
                
                counter[answerKey[slow]] -=1
                slow +=1
                
            res = max(res, fast - slow +1)
            
        return res
                