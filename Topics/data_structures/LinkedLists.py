
class SlinkedList:
    def __init__(self):
        self.head_node = None
    
    def printList(self):
        Slist = self.head_node
        while Slist:
            print(Slist.data_val)
            Slist = Slist.next_node

class Node:
    def __init__(self, data_val = None):
        self.data_val = data_val
        self.next_node = None

One = SlinkedList()
One.head_node = Node('One')
Two = Node('Two')
Three = Node("Three")
Four = Node(4)

One.head_node.next_node = Three
Three.next_node= Two
Two.next_node = Four

One.printList()