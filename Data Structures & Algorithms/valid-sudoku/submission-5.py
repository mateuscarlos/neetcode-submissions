#solução vídeo Solo 1 - TC:O(n^2)|SC:(n)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}

        for r in range(len(board)):
            for c in range(len(board[0])):
                elem = board[r][c]
                if elem != ".":
                    if r not in rows:
                        rows[r] = set()
                    if c not in cols:
                        cols[c] = set()
                    if (r // 3, c // 3) not in squares:
                        squares[(r // 3, c // 3)] = set()
                    if (elem in rows[r]) or (elem in cols[c]) or (elem in squares[(r // 3, c // 3)]):
                        return False
                
                    rows[r].add(elem)
                    cols[c].add(elem)
                    squares[(r//3, c//3)].add(elem)
        return True
