class Node:
    def __init__(self, data):
        self.data=data
        self.right = None
        self.left = None
    
    def insert(self, data):
        if data < self.data:
            if not self.data.left:
                self.data.left = Node(data)
            else: 
                self.insert(data)
        elif data > self.data:
            if not self.data.right:
                self.data.right = Node(data)
            else: 
                self.insert(data)
        
            