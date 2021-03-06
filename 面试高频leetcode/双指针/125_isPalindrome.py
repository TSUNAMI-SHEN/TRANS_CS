class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        return True
