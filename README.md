# Min Heap
Heap structure is a heap queue described in MIT lecture ["Heaps and Heap Sort"](https://www.youtube.com/watch?v=B7hVxCmfPtM). This repository contain implementation of Min Heap which was only mentioned there and is based on Max Heap description from MIT lecture.

## Structure
Min Heap is a queue structure. The root of a it contain the smallest value from iterable array. Every parent is smaller than his children. It is ensured by min_heapify() method. If node n has children, first is in node 2n+1 and second in node 2n+2. For example 10 items array will be represented as below:
</br>
![Min Heap tree](img/min_heap_tree.png)
</br>
To get Min Heap queue below methods can be used:
- min_heap - iterate from the last parent to the root
- min_heapify - check if parent node is smaller than children nodes
- exchange - swap 2 values ​​with each other

## Example
To visualize Min Heap example iterable array can be used:
```python
iterable_array = [5, 2, 8, 1, 4, 14, 6, 11, 25, 3]
```
This array can be visualized as a tree:
</br>
![Min Heap step 1](img/min_heap_step1.png)
</br>
For the last parent (node 4) function min_heapify is called. It calls exchange method because parent node is bigger than child node. After swapping min_heapify is fulfilled.
</br>
![Min Heap step 2](img/min_heap_step2.png)
</br>
In the next step node 3 is processed and it has value smaller than his children so nothing changes.
</br>
![Min Heap step 3](img/min_heap_step3.png)
</br>
Nodes 2 and 1 are processed similar to node 4.
</br>
![Min Heap step 4](img/min_heap_step4.png)
![Min Heap step 5](img/min_heap_step5.png)
</br>
Handling case of node 0 after exchange min_heapify rule isn't done so exchange method should be executed also for changed child.  After that min_heapify is fulfilled.
</br>
![Min Heap step 6](img/min_heap_step6.png)
![Min Heap step 7](img/min_heap_step7.png)
</br>
Final Min Heap queue form:
</br>
![Min Heap step 8](img/min_heap_step8.png)
</br>
Array in Min Heap structure is equal:
```python
[1, 2, 6, 5, 3, 14, 8, 11, 25, 4]
```
## Heapq library
Min Heap is implemented in [heapq](https://docs.python.org/3.0/library/heapq.html) library as `nsmallest` method. 
