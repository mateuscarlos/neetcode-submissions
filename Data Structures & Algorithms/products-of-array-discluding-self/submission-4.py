#gemini
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Inicializamos o array de resposta
        ans = [] 
        
        # 'left' guardará o produto acumulado de todos os elementos à esquerda de i
        left = 1
        
        # PRIMEIRA PASSADA: Da esquerda para a direita
        for i in range(len(nums)):
            # Colocamos o produto acumulado atual na resposta
            ans.append(left)
            # Atualizamos o acumulador multiplicando pelo número atual para o próximo índice
            left *= nums[i]
        
        # Agora 'ans' contém os produtos dos prefixos. 
        # Ex: para [1, 2, 3, 4], 'ans' é [1, 1, 2, 6]
        
        # 'right' guardará o produto acumulado de todos os elementos à direita de i
        right = 1
        
        # SEGUNDA PASSADA: Da direita para a esquerda (de len-1 até 0)
        for i in range(len(nums) - 1, -1, -1):
            # Multiplicamos o que já está lá (prefixo) pelo acumulador da direita (sufixo)
            ans[i] *= right
            # Atualizamos o acumulador da direita para o próximo índice (andando para a esquerda)
            right *= nums[i]

        return ans