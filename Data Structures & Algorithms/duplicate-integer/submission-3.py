from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hash set vazio
        seen = set()
        for n in nums:
            if n in nums:
                if n in seen:
                    return True
                seen.add(n)
        return False
        