#dicionario TC.: O(n * nlogn) - SC.:O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1

        arr = []
        for n in freq:
            arr.append([freq[n], n])

        arr.sort()

        ans = []
        for _ in range(k):
            ans.append(arr.pop()[1])

        return ans