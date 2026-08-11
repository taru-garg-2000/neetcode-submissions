import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = [(count, num) for num, count in counts.items()]
        heapq.heapify_max(heap)

        return [heapq.heappop_max(heap)[1] for _ in range(k)]
