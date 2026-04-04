class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        l = 0
        fruits_freq = defaultdict(set)

        for r, fruit in enumerate(fruits):
            fruits_freq[fruit] = fruits_freq.get(fruit, 0) + 1
            while len(fruits_freq) > 2:
                fruit_l = fruits[l]
                fruits_freq[fruit_l] -= 1
                if fruits_freq[fruit_l] == 0:
                    del fruits_freq[fruit_l]
                l += 1
            max_fruits = max(max_fruits, (r - l + 1))
        return max_fruits


        