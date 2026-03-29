#dicionario otimizado solo
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord("a")] += 1
            word_key = tuple(word)
            if word_key not in hashMap:
                hashMap[word_key] = []
            hashMap[word_key].append(s)
        return list(hashMap.values())