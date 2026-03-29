#gemini
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Codificamos como: [TAMANHO] + [DELIMITADOR] + [CONTEÚDO]
            # O '#' serve apenas para sabermos onde o número do tamanho termina.
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        # O ponteiro 'i' marca o início de cada "pacote" (ex: o início do número 4 em "4#neet")
        while i < len(s):
            # O ponteiro 'j' vai procurar o próximo delimitador '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # s[i:j] contém os dígitos do número (ex: se for "12#...", pega o "12")
            length = int(s[i:j])
            
            # Agora sabemos exatamente quantos caracteres ler após o '#'
            # O '#' está na posição j, então a string começa em j + 1
            # E termina em j + 1 + length
            res.append(s[j + 1 : j + 1 + length])
            
            # Movemos 'i' para o início do próximo pacote
            # j + 1 (pula o #) + length (pula a palavra que acabamos de ler)
            i = j + 1 + length
            
        return res
