class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = (end + start) // 2
            if nums[middle] == target:
                return middle

            if nums[start] <= nums[middle]:
                if target > nums[middle] or target < nums[start]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if target < nums[middle] or target > nums[end]:
                    end = middle - 1
                else:
                    start = middle + 1
        return -1