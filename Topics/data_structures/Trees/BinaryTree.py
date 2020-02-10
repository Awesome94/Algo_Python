class Node:
    def __init__(self, data=None):
        self.data=data
        self.right = None
        self.left = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else: 
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else: 
                    self.right.insert(data)
     
    
    def findval(self, data):
        if not self.data:
            return " no data to search"
        if data < self.data:
            if not self.left:
                return "not found at all"
            return self.left.findval(data)
        elif data > self.data:
            if not self.right:
                return "not found on the right"
            return self.right.findval(data)
        else:
            print(self.data, "is found")
        

    def print_tree(self, data):
        if self.left:
            self.left.print_tree(data)
        print(self.data)
        if self.right:
            self.right.print_tree(data)
            
root = Node(8)
root.insert(12)
root.insert(6)
root.insert(4)
root.insert(3)

root.print_tree(12)

print(root.findval(7))
print(root.findval(12))