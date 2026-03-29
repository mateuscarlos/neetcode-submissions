#video com comentarios gemini
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Inicializamos dicionários para mapear as três regras de validação.
        # As chaves identificarão a 'região' (índice da linha, col ou tupla do quadrado)
        # e os valores serão conjuntos (sets) para garantir unicidade.
        rows = dict()
        cols = dict()
        squares = dict()

        # Percorremos cada célula do tabuleiro usando índices de linha (r) e coluna (c).
        for r in range(len(board)):
            for c in range(len(board)):
                elem = board[r][c]
                
                # Células vazias (".") não possuem restrições, por isso as ignoramos.
                if elem != ".":
                    
                    # Verificamos se a chave da linha/coluna/quadrado já existe no dicionário.
                    # Se não existir, criamos um novo set vazio para aquela região específica.
                    # Isso evita erros de "KeyError" ao tentar acessar a região pela primeira vez.
                    if r not in rows:
                        rows[r] = set()
                    if c not in cols:
                        cols[c] = set()
                    
                    # O cálculo (r // 3, c // 3) agrupa coordenadas de 0 a 8 em blocos de 0 a 2.
                    # Ex: Células (0,0) e (2,2) ambas resultam na chave (0,0), o primeiro quadrado.
                    if (r // 3, c // 3) not in squares:
                        squares[(r // 3, c // 3)] = set()
                    
                    # Verificamos a regra de ouro: se o elemento já está presente em qualquer
                    # um dos conjuntos da sua respectiva linha, coluna ou quadrado.
                    if (elem in rows[r]) or (elem in cols[c]) or (elem in squares[(r // 3, c // 3)]):
                        # Se encontrar uma duplicata, a regra foi violada.
                        return False

                    # Caso o número seja novo naquela região, nós o adicionamos aos três registros.
                    # Assim, ele será detectado se aparecer novamente nesta iteração ou nas próximas.
                    rows[r].add(elem)
                    cols[c].add(elem)
                    squares[(r // 3, c // 3)].add(elem)
        
        # Se o loop terminar sem encontrar duplicatas, o tabuleiro é válido.
        return True