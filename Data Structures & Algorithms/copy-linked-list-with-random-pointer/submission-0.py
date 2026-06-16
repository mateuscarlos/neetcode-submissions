"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #inicia um hashmap para armazenar as cópias.
        #inicializa com valores mapeados None : None para o caso de algum ponteiro, next ou random apontar para None
        oldToCopy = {None : None}

        #primeiro loop para guardar os valores no hashmap
        cur = head #indica que o ponteiro cur inicia pela head da lista
        while cur:
            copy = Node(cur.val) #cria a variável copy para armazenar o valor do nó
            oldToCopy[cur] = copy #atribui o valor da variável copy ao dicionário na posição do valor cur
            cur = cur.next #atualiza o valor de cur para o próximo item da lista para continuar percorrendo os nós

        #segundo loop para atribuir as ligações dos nós
        cur = head #reatribui o valor do head à variável cur
        while cur:
            copy = oldToCopy[cur] #cria a variável copy e atribui a ela o valor armazenado no hashmap na posição da variável cur
            copy.next = oldToCopy[cur.next]#atribui a ligação next ao valor no dicionário na posição cur.next
            copy.random = oldToCopy[cur.random]#atribui a ligação random ao valor no dicionário na posição cur.random
            cur = cur.next #atualiza o ponteiro cur para o próximo nó da lista
            
        return oldToCopy[head] #retorna a lista atualizada armazenada no dicionário(hashmap)