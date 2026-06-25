class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum,s)).lower()
        
        if new_s[::-1] == new_s:
            return True
        else:
            return False
        