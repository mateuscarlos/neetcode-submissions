#solução do vídeo
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #string codificada
        for s in strs: #para cada string no array de strings
            res += str(len(s)) + "#" + s #comprimento da string que é convertido para string + delimitador + string em si => formato combinado
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #array (lista) recebida codificada. 
                        #Vou iterar usando o ponteiro i que dirá onde estamos da string de entrada
                        #começando no índice 0 até o fim do array
        while i < len(s): #enquanto i estiver dentro dos limites leremos caractere por caractere. 
                            #Quando o loop iniciar, a primeira posição será um inteiro
            #agora vamos buscar o delimitador
            j = i
            while s[j] != "#": #enquanto o ponteiro j for diferente do carcatere delimitador
                j += 1 #continuaremos incrementando j em 1
            length = int(s[i:j]) #essa será a parte inteira que estará convertida novamente para inteiro
            res.append(s[j + 1 : j + 1 + length])#começamos a string em j porque j é o caractere delimitador
                                                    #str[primeiro caractere pós # + ele mesmo + o comprimento da string]
                                                    #res.append anexa ela ao resultado
            i = j + 1 + length #isso poderá ser o início da próxima string ou o final da última
        return res

