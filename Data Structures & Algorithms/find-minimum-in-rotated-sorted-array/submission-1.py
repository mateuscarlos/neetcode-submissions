class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

            middle = (start + end) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[start]:
                start = middle + 1
            else:
                end = middle - 1
        return res