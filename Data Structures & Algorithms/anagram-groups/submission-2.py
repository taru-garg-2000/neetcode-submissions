from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)

        ans = []

        for s in m:
            ans.append(m[s])

        return ans