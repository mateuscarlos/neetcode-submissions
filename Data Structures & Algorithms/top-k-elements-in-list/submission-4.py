class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap de contagem de valor
        freq = [[] for i in range(len(nums) + 1)] #matriz com o mesmo tamanho da matriz de entrada + 1

        for n in nums: #percorre cada valor em num e contar quantas vezes cada 1 ocorre
            count[n] = 1 + count.get(n, 0) #o 0 está ali para o caso de um valor não estar ainda no hash
        for n, c in count.items():
            freq[c].append(n)

        #Percorre os baldes de trás para frente (da maior frequência para a menor). 
        #Assim, os elementos mais frequentes entram primeiro em res. 
        # Assim que res atinge o tamanho k, o algoritmo retorna imediatamente — sem precisar percorrer o restante.
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res