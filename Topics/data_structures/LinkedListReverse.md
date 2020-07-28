This article will focus oly on the core functionality of reversing both a singly linked list and a doubly linked list.

Singly linked list:(Focus on nextNode)
- Most confusion or errors/difficulties around reversing linked lists is the order of assigning variables. It can be challenging to understand and get right in a short time.
Function to reverse a singly Linked List
```python
def reverse(head):
    node = head
    NextNode = None
    PrevNode = None
    while node:
        NextNode = node.next
        node.next = PrevNode
        PrevNode = node
        node = NextNode
    self.head = PrevNode
```

### Reversing A Doubly Linked List.
- Now here, unlike the singly linked list, In the doubly linked list we shall priotize the previous node hence node.prev.

Below is a function to reverse a doubly linked list.

```python
def reverse(head):
    node = head
    PrevNode = None
    while node:
        PrevNode = node.prev
        node.prev = node.next
        node.next = PrevNode
        node = node.prev
    self.head=PrevNode.prev

```

### Remove Duplicates from Linked List.
``` python
    def remove_duplicates(head):
        node = head
        collection = []
        while node:
            if node in collection:
                node.prev.next = node.next
            else:
                collection.append(node)
            node = node.next
            
```