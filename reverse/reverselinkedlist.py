def reverseLinkedlist(Node head):
    if head == null:
        return
    reversedLinkedlist(head.next)
    return head.value


    