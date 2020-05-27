"""
Question One
Given a head of a singly linked list, write a function to determine if the Linked List has a cycle in it or not.
"""

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
def hasCycle(self, head):
    slow,fast = head, head
    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True #Found cycle
    return False
#will run in O(N) => N being the number of nodes since the cycle will be found in the first loop.


"""
LENGTH OF THE CYCLE
Given the head of a linked list with a cycle, find the length of the cycle. 

"""

def findCycleLength(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return find_cycle_length(slow)
    return 0

def find_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length+=1
        if current == slow:
            break
    return cycle_length

"""

"""