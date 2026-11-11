#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reverseKGroup(self, head, k):
#         pl = ListNode(0)
#         pl.next = head
#         pr = pl
#         while pr.next and pr.next.next: # Цикл выполняется до тех пор, пока перед указателем pr есть хотя бы два узла (полная пара). Если остаётся 1 узел или список закончился, цикл останавливается.
#                 first = pr.next # запоминаем первый узел пары (1).
#                 second = pr.next.next # запоминаем второй узел пары (2).
#                 first.next = second.next # Узел 1 отцепляется от 2 и начинает указывать на узел 3 (на следующий элемент после пары)
#                 second.next = first # Узел 2 указывает на узел 1. Теперь порядок пары изменился на 2 -> 1.
#                 pr.next = second # Предыдущий узел (0) подсоединяется ко второму узлу (2), фиксируя новую последовательность: 0 -> 2 -> 1 -> 3 -> 4.
#                 pr = first    #Указатель pr сдвигается на узел 1. На следующей итерации он будет стоять прямо перед парой 3 и 4.
#         return pl.next
# head = [1,2,3,4,5]
# k = 2
def ass(head, k):
    arr = []
    l = len(head)
    if l < k:
        return head
    elif l == k:
        return head[::-1]
    else:
        for i in range(0,l,k):
            gl = head[i:i+k]
            if len(gl) == k:
                arr.extend(gl[::-1])
            else: arr.extend(gl)
        return arr
head = [1,2,3,4,5]
k = 2
ans = ass(head,k)
print(ans)