class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1

                w_key = tuple(w)

            groups[tuple(count)].append(w)

        return list(groups.values())


                