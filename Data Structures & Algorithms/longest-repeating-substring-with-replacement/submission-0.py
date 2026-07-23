class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxlen = 0
        seen = {}
        maxfreq = 0

        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right],0) + 1

            maxfreq = max(maxfreq,seen[s[right]])

        
            while (right - left +1) - maxfreq > k:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                
                left +=1
            
            maxlen = max(maxlen,right - left +1)

        return maxlen
                

        
        