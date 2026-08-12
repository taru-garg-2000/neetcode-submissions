from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        low = 0
        high = 0
        counts = defaultdict(int)

        while high < len(s):
            while high < len(s):
                counts[s[high]] += 1
                if counts[s[high]] > 1:
                    break
                high += 1
                
            # print(high, low, res)
            res = max(res, high - low)

            if high < len(s):
                while counts[s[high]] > 1:
                    counts[s[low]] -= 1
                    low += 1

            high += 1

        return res