#### Binary Trees.
A tree can have multiple child nodes. A tree with more than two nodes is called a tenary Tree where as a binary tree can only have a maximum of two childe nodes. 
i.e the left and right node.

A child node without a child node is known as a "leaf" node. 

Implementation of A Binary Tree with Python.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left  = None
```
A Tree does not necesarily have the child nodes pointing back to the parent Node. Also not compulsory for a tree to have a root node.

After Initializing out Binary Tree, we have to add data to it. Expanding on the above class, we are going to add a new function called `inset` to allow us to insert data into our binary tree. Before inserting the data into the binary tree, we have to make sure that Tree satisifies the condition that the nodes to the left of the parent Node are less or equal to the Parent Node and that the  nodes to the right of the parent Node are greater than or equal to the Parent Node and that will be reflected during  `insertion` as seen in the `insert` function below.

```python
class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None
        self.left = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right= Node(data)
                self.right.insert(data)
        self.data = Node(data)

```