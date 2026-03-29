class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        heap = []

        for n in freq:
            heapq.heappush(heap, [freq[n], n])
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans