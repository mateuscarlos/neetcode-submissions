class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        seen = defaultdict(list)  # mais limpo que if not in
        
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord('a')] += 1
            seen[tuple(word)].append(s)  # direto, sem if
        
        return list(seen.values())