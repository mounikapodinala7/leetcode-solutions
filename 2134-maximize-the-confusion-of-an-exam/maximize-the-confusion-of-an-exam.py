class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def longest_with_char(target):
            left = 0
            changes = 0
            max_len = 0
            
            for right in range(len(answerKey)):
                if answerKey[right] != target:
                    changes += 1
                
                while changes > k:
                    if answerKey[left] != target:
                        changes -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len
        
        return max(longest_with_char('T'), longest_with_char('F'))
