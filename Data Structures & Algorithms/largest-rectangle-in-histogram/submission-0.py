class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Vai guardar tuplas: (index_inicial, altura)

        for i, h in enumerate(heights):
            start = i
            # Enquanto a barra do topo da pilha for maior que a barra atual
            while stack and stack[-1][1] > h:
                p_start, p_height = stack.pop()
                # A largura vai do índice inicial daquela barra até o índice atual 'i'
                maxArea = max(maxArea, p_height * (i - p_start))
                # O 'start' da barra atual é estendido para trás
                start = p_start
            
            stack.append((start, h))

        # Para as barras que conseguiram chegar até o final do histograma
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea