### Helper classes were implemented locally in "linked_list_helper.py" to enable local execution

from linked_list_helper import LinkedList, ListNode

def pairSum(head: ListNode) -> int:
        left_stack = []
        list_len = 0
        pointer = head

        while pointer:
            list_len += 1
            pointer = pointer.next

        center_left = list_len / 2 - 1
        counter = 0
        max_pair = -10000

        while counter < list_len and head:
            if counter <= center_left:
                left_stack.append(head.val)
            else:
                left = left_stack.pop()
                val = head.val
                max_pair = max(max_pair, left + val)
            counter += 1
            head = head.next
        
        return max_pair

if __name__ == '__main__':
    print('testes')
    print(pairSum(LinkedList([5,4,2,1]).head) == 6)
    print(pairSum(LinkedList([4,2,2,3]).head) == 7)
    print(pairSum(LinkedList([1,10000]).head) == 10001)