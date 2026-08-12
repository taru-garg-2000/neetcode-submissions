from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        total = len(t)
        count_t = Counter(t)
        count_s = defaultdict(int)
        l, r, ans, ans_len = 0, 0, "", float('inf')

        if len(t) > len(s):
            return ""

        while r < len(s):
            # 1. Expand until all characters in t are satisfied
            while total != 0 and r < len(s):
                if count_s[s[r]] < count_t[s[r]]:
                    total -= 1
                count_s[s[r]] += 1
                r += 1

            while l < r and total == 0:
                if r - l < ans_len:
                    ans_len = r - l
                    ans = s[l:r]

                count_s[s[l]] -= 1
                if count_s[s[l]] < count_t[s[l]] and count_t[s[l]] != 0:
                    total += 1
                l += 1
        return ans

