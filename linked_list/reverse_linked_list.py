### Helper classes were implemented locally in "linked_list_helper.py" to enable local execution

from linked_list_helper import LinkedList, ListNode

def reverseList(head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev

if __name__ == '__main__':
    print('testes')
    print(repr(reverseList(LinkedList([1,3,4,7,1,2,6]).head)) == '6217431')
    print(repr(reverseList(LinkedList([1,2,3,4]).head)) == '4321')
    print(repr(reverseList(LinkedList([2,1]).head)) == '12')