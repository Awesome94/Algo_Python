#### Tree.
A tree represents nodes connected by edges. A tree can have multiple child nodes. A tree with more than two nodes is called a tenary Tree whereas a binary tree can only have a maximum of two child nodes.

#### Binary Trees.
Binary Tree is a special datastructure used for data storage purposes. A binary tree has a special conditon i.e. each node can have a maximum of two children. 
A Binary tree has fast insertion, deletion and search time.



A child node without a child node is known as a "leaf" node. 

Implementation of A Binary Tree with Python.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left  = None
```
A Tree does not necessarily have the child nodes pointing back to the parent Node. Also not compulsory for a tree to have a root node.

After Initializing out Binary Tree, we have to add data to it. Expanding on the above class, we are going to add a new function called `insert` to allow us to insert data into our binary tree. Before inserting the data into the binary tree, we have to make sure that Tree satisfies the condition that the nodes to the left of the parent Node are less or equal to the Parent Node and that the nodes to the right of the parent Node are greater than or equal to the Parent Node and that will be reflected during  `insertion` as seen in the `insert` function below.

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
    
    def search(self, data):
        if self.data == data:
            return data
        if data < self.data:
            self.search(self.left)
        elif data > self.data:
            self.search(self.right)

```
### Traversing a Tree.
- Inorder Traversal
- Preorder Traversal
- PostOrder Traversal

Implementation of the above traversals in python

```python
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    # Inorder Traversal
    def PrintInorder(root):
        if root:
            PrintInorder(root.left)
            print(root.val)
            PrintInorder(root.right)

    def PrintPreorder(root):
        if root:
            print(root.val)
            PrintPreorder(root.left)
            PrintPreorder(root.right)

    def PrintPostOrder(root):
        if root:
            PrintPostOrder(root.left)
            PrintPostOrder(root.right)
            print(root.val)

    def IsBalanced(root):
        if root:
            if root.left > root.val or root.val > root.right:
                return False
            IsBalanced(root.right)
            IsBalanced(root.left)
        return True
```
### Breadth First Search(BFS) aka level order Traversal