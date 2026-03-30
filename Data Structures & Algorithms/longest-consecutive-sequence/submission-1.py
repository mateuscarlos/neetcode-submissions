#ordenação - TC: O(n log n)|SC: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(len(nums) -1):
            if nums[i + 1] != nums[i]:
                if nums[i + 1] -1 == nums[i]:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1
        
        return longest