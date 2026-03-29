class Solution:

    def encode(self, strs: List[str]) -> str:
        #para cada string, prefixamos com seu cumprimento e '#'
        #Exemplo: #Hello# -> #5#Hello"
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 #ponteiro que percorre a string codificada

        while i < len(s):
            #Passo 1: Procurar o "#" para saber onde termina o número
            j = i
            while s[j] != "#":
                j += 1
            
            # Passo 2: extrair o comprimento da próxima string
            length = int(s[i:j])

            # Passo 3: extrair exatamente 'length' caracteres após o '#'
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Passo 4: mover o ponteiro para após a string que acabamos de ler
            i = j + 1 + length

        return result