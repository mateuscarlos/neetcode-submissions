from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # Usamos defaultdict para evitar erros ao acessar chaves que ainda não existem.
    # Cada chave terá como valor uma lista []
        anagram_map = defaultdict(list)

        for s in strs:
            # 1. Ordenamos a string: 'eat' vira ['a', 'e', 't']
            # 2. Juntamos de volta: 'aet'
            # 3. Usamos isso como chave (identificador único do anagrama)
            sorted_s = "".join(sorted(s))

            # Adicionamos a palavra original na lista correspondente àquela chave
            anagram_map[sorted_s].append(s)

        # Retornamos apenas os valores do dicionário (as listas agrupadas)
        return list(anagram_map.values())