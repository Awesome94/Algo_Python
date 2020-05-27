"""
Implementation of a foubly linked list
A doubly linked List has got two pointers i.e.:
    - Pointer to the next node and pointer to the previous node.
"""
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, newNode):
        new_Node = Node(newNode)
        if self.head == None:
            self.head = new_Node
        self.head.prev = new_Node

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def reverse(self):
        curr = self.head
        prevNode=None
        while curr:
            prevNode = curr.prev
            curr.prev = curr.next_node
            curr.next_node = prevNode
            curr = curr.prev
        self.head = prevNode.prev

dlist = DoublyLinkedList()
dlist.head = 12

"""
Doubly linked list can be implemented with the collections.deque module in python.
A deque is a double sided queue hence data can be accessed from both directions .

so basically for the doubly linked list we perform the following commands.
Append:
    -Add element at the end of the List 
    That can be completed in the following steps:
        - if self.head is None, self.head = Node
        - while head:
        - head = head.nextNode
        - head.nextNode = Node(newNode)
Prepend:
    - Add element at the begining of the list
    That can be completed in the following steps:
        - IF self.head is None:
        - self.head = Node(newNode)
        - self.head.prev = Node(newNode)
find Key:
    - curr = self.head:
    - while curr and curr.data != Key:
    - curr = curr.next
    - return curr
Remove Key 
Insert before Node
    - Add element before a specific node
        - make sure that the node we are trying to insert is not the head and tail node. 
        - remove any existing instances of the node we are trying to insert.
        - nodeToInsert.prev = node.prev
        - nodeToInsert.next = node
        if node.prev is none:
            self.head == nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
Insert After Node
Remove Element
"""