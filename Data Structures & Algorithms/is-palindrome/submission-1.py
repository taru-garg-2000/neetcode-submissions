class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [a.lower() for a in s if a.isalnum()]

        for i in range(len(x)//2):
            if x[i] != x[len(x)-i-1]:
                return False

        return True