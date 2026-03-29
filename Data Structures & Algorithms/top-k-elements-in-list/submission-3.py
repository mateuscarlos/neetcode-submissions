import heapq # Biblioteca padrão para Heaps em Python

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Passo 1: Contar as frequências O(N)
        # Criamos um dicionário onde a chave é o número e o valor é a frequência
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Passo 2: Construir o Heap O(N log K)
        # O heap guardará tuplas: (frequência, número)
        # Python implementa um MIN-HEAP (o menor valor fica sempre no topo/índice 0)
        min_heap = []
        
        for num, freq in count.items():
            # Adicionamos o par ao heap
            heapq.heappush(min_heap, (freq, num))
            
            # Se o tamanho do heap exceder K, removemos o menor
            # Como é um Min-Heap, o heapq.heappop remove o item com MENOR frequência
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Passo 3: Extrair os resultados O(K)
        # O que sobrou no heap são os K elementos com maior frequência
        return [n for f, n in min_heap]