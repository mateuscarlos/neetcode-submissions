#força bruta - TC:O(n^2)|SC: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            fator_multi = 1
            for j in range(len(nums)):
                if i != j:
                    fator_multi *= nums[j]
                
            ans.append(fator_multi)
        return ans
