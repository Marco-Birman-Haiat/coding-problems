### Helper classes were implemented locally in "linked_list_helper.py" to enable local execution

from linked_list_helper import LinkedList, ListNode

def deleteMiddle(head: ListNode):
    nodeCount = 0
    a = head
    
    if head.next == None:
        return None
    while a != None:
        nodeCount += 1
        a = a.next

    middle = nodeCount // 2
    if nodeCount == 2:
        head.next = None
        return head

    a = head
    for _ in range(middle - 1):
        a = a.next
    
    a.next = a.next.next
    return head

if __name__ == '__main__':
    print('testes')
    print(repr(deleteMiddle(LinkedList([1,3,4,7,1,2,6]).head)) == '134126')
    print(repr(deleteMiddle(LinkedList([1,2,3,4]).head)) == '124')
    print(repr(deleteMiddle(LinkedList([2,1]).head)) == '2')