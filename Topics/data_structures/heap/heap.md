## HEAPS
A heap is a special tree structure. It can be categorized into the:
    1. Max heap.
    2. A min heap

#### Max Heap:
A tree structure in which the parent node is greater than or equal to the child nodes.

#### Min Heap:
A tree structure in which the parent node is smaller/less than or equal to the child nodes

##### Creating A heap
A heap can be created using python's inbuilt library called the `heapq` library which contains several functions 
```python
import heapq
H = [2,23,1,0,9]
heapq.heapify(H)
Print(H)

# Remove irem from heap using `heapop`
heapq.heappop(H)
print(H)
# Repalacing in a heap
heapq.heapreplace(H, 6)
print(H)
```
#### OutPut
``` 
[0, 1, 2, 9, 23]

[0, 1, 2, 9]

[1, 2, 6, 9, 23]
```
### Creating a heap from a given array/list H
heapq.heapify(H)

### Removing an element from heap
- Pops the last element from the heap.
heapq.heappop(H)

### Replacing an element in the heap.
- Takes in the name of the list and the new element to add to the heap as params. The new element to add will replace the current minimum in the heap

heapq.heapreplace(H, 6)
