# Linked List cycle 
# Solved using the hare and tortoise approach

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = None

def hasCycle(head):
    fast=slow=head
    while fast and  fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False 