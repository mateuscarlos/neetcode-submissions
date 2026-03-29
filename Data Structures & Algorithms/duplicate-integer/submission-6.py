from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Cria um hash para armazenar os números encontrados
        seen = set()

        for n in nums:
            if n in nums:
                #varre o hash para seu conteúdo
                if n in seen:
                    #retorna verdadeiro se o número já estiver no hash
                    return True
                    #adiciona um número se ele ainda não tiver no hash
                seen.add(n)
        return False
                
        