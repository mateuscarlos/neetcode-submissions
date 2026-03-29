import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contagem de frequências
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # 2. Usar um Min-Heap para manter apenas os K elementos mais frequentes
        # Em Python, heapq é um min-heap por padrão
        heap = []

        for num, freq in count.items():
           # Empurramos (frequência, número) para o heap
           heapq.heappush(heap, (freq, num))

           # Se o heap ficar maior que k, removemos o que tem MENOR frequência
           if len(heap) > k:
            heapq.heappop(heap)

        # 3. Extraímos apenas os números do nosso heap de tamanho k
        return [pair[1] for pair in heap]