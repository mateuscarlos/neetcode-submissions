#forca bruta
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: #TC.: O(n^2)
        ans = [] #lista com os produtos

        for i in range(len(nums)): #para cada numero i no intervalo de comprimento do array =>O(n)
            factor_multi = 1
            for j in range(len(nums)): # => O(n)
                if i != j:
                    factor_multi *= nums[j]
            ans.append(factor_multi)
        return ans