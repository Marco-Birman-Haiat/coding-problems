class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self) -> str:
        result = []
        helper = self
        while helper:
            result.append(str(helper.val))
            helper = helper.next
        return ''.join(result)

class LinkedList():
    def __init__(self, node_data) -> None:
        self.head = ListNode()
        self.populate_linked_list(node_data)
    
    def populate_linked_list(self, node_data):
        helper = self.head
        if len(node_data):
          for value in node_data:
              helper.next = ListNode(value)
              helper = helper.next
          self.head = self.head.next
    
        