#soluçao do vídeo
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}#conta as ocorrencias de cada valor
        freq = [[] for i in range(len(nums) + 1)]
        #matriz que terá o mesmo tamanho da matriz de entrada. 
        #O indice será a frequencia de 1 elemento ou a contagem de 1 elemento 
        #o valor será a lista de valores que ocorrem aquele número específico de vezes e por isso inicializa vazio
        #o numero de matrizes vazias que entram será o tamanho da entrada + 1
        for n in nums: #para cada numero em nums
            count[n] = 1 + count.get(n, 0)
            #contar quantas vezes ele ocorre
            #cada numero + sua contagem atual
            #colocamos um valor padrão de 0 para que o retorno seja 0 se ele não existir
        for n, c in count.items(): #para cada numero e (quem é c?) nos itens da contagem
            freq[c].append(n)#diz que o valor n ocorre exatamente c vezes

        res = [] #saída de resultado - queremos os "k" primeiros elementos
        for i in range(len(freq) - 1, 0, -1):#para i no intervalo de comprimento de freq -1 
                                            #(que adicionamos para que o cumprimento ignorasse o indice 0).
                                            #Vamos até 0 e em ordem decrescente. O -1 é decrementador
            for n in freq[i]: #para cada valor n na matriz freq neste indice i
                res.append(n)
                if len(res) == k:
                    return res
