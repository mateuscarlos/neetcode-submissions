#prefixo e sufixo - TC: O(n)|SC: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = 1

        for i in range(len(nums)):
            ans.append(left)
            left *= nums[i]

        right = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
