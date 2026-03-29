from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Criamos um dicionário onde o valor padrão é uma lista vazia
        res = defaultdict(list)

        for s in strs:
           # Criamos um array de 26 zeros, um para cada letra (a-z)
           count = [0] * 26

           for char in s:
               # Calculamos o índice da letra usando a tabela ASCII
               # ord('a') é 97. Se char for 'b' (98), 98 - 97 = índice 1
               count[ord(char) - ord("a")] += 1

           # Convertemos a lista 'count' em tupla para ser usada como chave
           # Listas são mutáveis e não podem ser chaves de dicionário em Python
           res[tuple(count)].append(s)

        return list(res.values())