class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord('a')] += 1
            
            word_key = tuple(word)

            if word_key not in seen:
                seen[word_key] = []
            seen[word_key].append(s)

        return list(seen.values())