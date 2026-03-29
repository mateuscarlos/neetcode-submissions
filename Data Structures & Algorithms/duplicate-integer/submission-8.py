#força bruta solo 1

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False
            