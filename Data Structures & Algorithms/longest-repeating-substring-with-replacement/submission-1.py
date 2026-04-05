class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        
        count = {}
        l = r = 0
        res = 0
        freq_max = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            freq_max = max(freq_max, count[s[r]])

            if (r - l + 1) - freq_max > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1
        return res