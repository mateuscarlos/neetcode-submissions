class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contar a frequência de cada número
        count = {}
        # Criamos 'baldes' de tamanho len(nums) + 1
        # freq[3] guardará todos os números que aparecem exatamente 3 vezes
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # 2. Preencher os baldes
        for n, c in count.items():
            freq[c].append(n)
        
        # 3. Coletar os resultados do balde mais alto para o mais baixo
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res