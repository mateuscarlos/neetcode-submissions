class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Transformamos a lista num SET para buscas O(1)
        num_set = set(nums)
        maior_sequencia = 0

        for n in num_set:
            # 2. Verificamos se 'n' é o início de uma sequência
            # Se (n - 1) não está no set, então 'n' é o ponto de partida
            if (n - 1) not in num_set:
                comprimento_atual = 1

                # 3. Enquanto o próximo número consecutivo existir, aumentamos a contagem
                while (n + comprimento_atual) in num_set:
                    comprimento_atual += 1

                maior_sequencia = max(maior_sequencia, comprimento_atual)

        return maior_sequencia