import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def rec(total, curr, idx):

            total = sum(curr)

            if  total == target:
                ans.append(copy.deepcopy(curr))
                return

            if total < target:
                for i in range(idx, len(candidates)):
                    num = candidates[i]

                    if i > idx and candidates[i] == candidates[i-1]:
                        continue
                    
                    if total + num > target:
                        break

                    if total + num <= target:
                        curr.append(num)
                        rec(total + num, curr, i+1)
                        curr.pop()

        rec(0, [], 0)
        return ans
                