class LinkedList:
    def __init__(self, value, next):
        self.value: value
        self.next: next
    def __str__(self):
        return f'{self.value}'

def find_middle_node_of_linked_list(ll):
    fast = ll
    slow = ll

    while fast != None or fast.next != None:
        fast = fast.next.next
        slow = slow.next

    return slow

