class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapear os caracteres e enviar a contagem para a lista de anagramas

        for s in strs:
            count = [0] * 26 #letras do alfabeto minusculas a ... z

            for c in s:
                count[ord(c) - ord("a")] +=1 #contagem de quantos caracteres temos, usando como referencia a tabela ASCII

            res[tuple(count)].append(s) #convertemos a lista para uma tupla pois em python as tuplas são imutáveis e como as listas não são, não podem ser chaves

        return list(res.values())