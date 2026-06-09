class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       counter = Counter(s1)
       window = Counter()
       left = 0

       for right in range(len(s2)):
        char_new = s2[right]
        window[char_new] += 1

        size = right - left + 1
        if size > len(s1):
            char_old=s2[left]
            window[char_old] -= 1

            if window[char_old] == 0:
                del window[char_old]

            left += 1
        
        if counter == window:
            return True
       return False