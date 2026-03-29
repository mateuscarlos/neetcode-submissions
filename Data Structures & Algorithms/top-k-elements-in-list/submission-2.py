class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contagem de frequências
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        # 2. Criar uma lista de itens (número, frequência)
        # Ex: [(1, 3), (2, 2), (3, 1)]
        items = list(count.items())

        # 3. Ordenar a lista pela frequência (x[1]) de forma decrescente
        items.sort(key=lambda x: x[1], reverse=True)

        # 4. Retornar os primeiros k números
        return [items[i][0] for i in range(k)]