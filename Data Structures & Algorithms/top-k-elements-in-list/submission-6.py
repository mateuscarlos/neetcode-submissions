import heapq # Biblioteca de Heap do Python (implementa um Min-Heap por padrão)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Contagem de frequência (igual às outras soluções)
        # O(n) de tempo
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Criar o Min-Heap
        # O objetivo é manter apenas os 'k' elementos mais frequentes no heap.
        heap = []
        
        for num, freq in count.items():
            # Inserimos uma tupla (frequência, número)
            # O heapq usa o primeiro elemento da tupla (frequência) para ordenar
            heapq.heappush(heap, (freq, num))
            
            # Se o tamanho do heap ultrapassar 'k', removemos o menor
            # Como é um Min-Heap, o menor elemento (menos frequente) está no topo
            if len(heap) > k:
                heapq.heappop(heap) # Remove o elemento com a menor frequência atual
        
        # 3. Extrair os números do heap
        # O heap agora contém exatamente os k elementos mais frequentes
        return [num for freq, num in heap]