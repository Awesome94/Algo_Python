class Node:
    def __init__(self, data_val = None):
        self.data_val = data_val
        self.next_node = None

class SlinkedList:
    def __init__(self):
        self.head_node = None
    
    def printList(self):
        Slist = self.head_node
        while Slist:
            print(Slist.data_val)
            Slist = Slist.next_node
    
    def addItemStart(self, newdata):
        newData = Node(newdata)
        newData.next_node = self.head_node
        self.head_node = newData
    
    def addItemEnd(self, newdata):
        newData = Node(newdata)
        if not self.head_node:
            self.head_node = newData
            return
        node = self.head_node
        while node.next_node:
            node = node.next_node
        node.next_node = newData
        


One = SlinkedList()
One.head_node = Node('One')
Two = Node('Two')
Three = Node("Three")
Four = Node(4)

One.head_node.next_node = Three
Three.next_node= Two
Two.next_node = Four
One.addItemStart(9)
One.addItemEnd(19)

One.printList()