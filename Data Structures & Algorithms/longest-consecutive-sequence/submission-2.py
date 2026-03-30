#dicionario - TC: O(n)|SC: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        longest = 1

        for num in nums_set:
            if (num - 1) not in nums_set:
                current = 1

                while num + current in nums_set:
                    current += 1

                longest = max(longest, current)
        
        return longest
