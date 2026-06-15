class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Garantimos que 'menor' seja sempre o array de menor tamanho
        # Isso torna a busca binária mais eficiente
        menor, maior = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    
        total_len = len(menor) + len(maior)
        metade = total_len // 2
    
        l, r = 0, len(menor) - 1
    
        while True:
            # i é o índice de corte no array menor (divisão inteira!)
            i = (l + r) // 2 
            # j é o índice de corte no array maior
            j = metade - i - 2 
        
            # Elementos ao redor do corte (usando -inf/+inf para bordas)
            esq_menor = menor[i] if i >= 0 else float("-infinity")
            dir_menor = menor[i + 1] if (i + 1) < len(menor) else float("infinity")
        
            esq_maior = maior[j] if j >= 0 else float("-infinity")
            dir_maior = maior[j + 1] if (j + 1) < len(maior) else float("infinity")
        
            # Verificamos se o corte está no lugar certo
            if esq_menor <= dir_maior and esq_maior <= dir_menor:
                # Se for ímpar, a mediana é o menor dos elementos da direita
                if total_len % 2:
                    return float(min(dir_menor, dir_maior))
                # Se for par, a média dos elementos centrais
                return (max(esq_menor, esq_maior) + min(dir_menor, dir_maior)) / 2
        
            # Ajustamos a busca binária
            elif esq_menor > dir_maior:
                r = i - 1
            else:
                l = i + 1