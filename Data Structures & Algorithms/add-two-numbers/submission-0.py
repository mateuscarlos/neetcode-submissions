# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0 #esse é o famoso "vai um" das operações de soma
        while l1 or l2 or carry: #enquanto houver nós ou carry for diferente de 0
            v1 = l1.val if l1 else 0 #atribui à variável v1 o valor do nó da lista 1. Se for nulo, atribui zero
            v2 = l2.val if l2 else 0 #atribui à variável v2 o valor do nó da lista 2. Se for nulo, atribui zero

            #calcula os valores dos novos digitos
            val = v1 + v2 + carry
            carry = val // 10 #atribui ao carry o valor da divisão inteira por 10. Exemplo: se for 12 o resultado será 1 que é o que precisamos
            val = val % 10 #atribui ao valor, o valor do resto de uma divisão por 10. Exemplo: se for 12, o resultado será 2 que o que precisamos
            cur.next = ListNode(val) #atribui ao próximo nó da nossa lista dummy o valor de val

            #atualização de ponteiros
            cur = cur.next #movimenta o ponteiro para o próximo nó
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None #atualiza as posições dos ponteiros para o próximo nó da lista
        
        return dummy.next #retorna a lista dummy criada