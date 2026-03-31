class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        for c in t:
            if (c not in freq) or (freq[c] <=0):
                return False
            freq[c] -= 1

        return True