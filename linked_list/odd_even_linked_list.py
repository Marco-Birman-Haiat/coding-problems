### Helper classes were implemented locally in "linked_list_helper.py" to enable local execution
from linked_list_helper import LinkedList, ListNode

def oddEvenList(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    
    odd = odd_head = head
    even = even_head = odd.next
    i = head.next.next
    counter = 0
    while i:
        if counter % 2 == 0:
            odd.next = i
            odd = i
        else:
            even.next = i
            even = i
        i = i.next
        counter += 1
    
    if even.next == odd:
        even.next = None
    
    odd.next = even_head
    return head

if __name__ == '__main__':
    print('testes')
    print(repr(oddEvenList(LinkedList([1,2,3,4,5]).head)) == '13524')
    print(repr(oddEvenList(LinkedList([2,1,3,5,6,4,7]).head)) == '2367154')
