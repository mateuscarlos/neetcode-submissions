class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Passo 1: Calcular os produtos à ESQUERDA (Prefixos)
        prefixo = 1
        for i in range(n):
            # O resultado no índice i recebe o produto de tudo antes dele
            res[i] = prefixo
            # Atualizamos o prefixo para o próximo elemento
            prefixo *= nums[i]

        sufixo = 1
        for i in range(n -1, -1, -1):
            # Multiplicamos o valor que já estava lá (prefixo) pelo sufixo atual
            res[i] *= sufixo
            # Atualizamos o sufixo para o próximo elemento à esquerda
            sufixo *= nums[i]

        return res