#!/usr/bin/env python
import heapq as pq
import numpy as np
import time


def exchange(iterable, i1, i2):
    '''
    Function to swap variables of iterable which indexes are i1 and i2.
    Params: iterable - iterable 1D array; 
            i1 - first index; 
            i2 - second index
    '''
    iterable[i1], iterable[i2] = iterable[i2], iterable[i1]


def min_heapify(iterable, i, key):
    '''
    Function to check if parent is smaller than children if not call exchange method.
    Params: iterable - iterable 1D array; 
            i - index to get parent node from iterable; 
            key - function which describe value of nodes
    '''
    child1 = 2*i+1
    child2 = 2*i+2
    try:
        if key(i) > min(key(child1), key(child2)):
            if key(child1) <= key(child2):
                exchange(iterable=iterable, i1=i, i2=child1)
                child = child1
            else:
                exchange(iterable=iterable, i1=i, i2=child2)
                child = child2
            if child < len(iterable)//2:
                min_heapify(iterable=iterable, i=child, key=key)
    except:
        if key(i) > key(2*i+1):
            exchange(iterable=iterable, i1=i, i2=child1)
            child = child1
        if child < len(iterable)//2:
            min_heapify(iterable=iterable, i=child, key=key)


def min_heap(iterable, key=None):
    '''
    Function to prepare Min Heap structure.
    Params: iterable - iterable 1D array; 
            key - function which describe value of nodes
    '''
    if key == None:
        heap_key = lambda x: iterable[x]
    else:
        heap_key = lambda x: key(iterable[x])

    for i in range(len(iterable)//2-1, -1, -1):
        min_heapify(iterable=iterable, i=i, key=heap_key)

    return iterable#[0]


if __name__ == '__main__':
    a = ['c', 'b', 'd', 'a', 'w']

    b = {'b': 1, 'c': 5, 'd': 7, 'a': 2, 'w': 10}

    print(f'a = {a}')
    print(f'b = {b}')

    print(f'Min Heap result for a: {min_heap(iterable=a)}')
    print(f'Min Heap from heapq library result for a: {pq.nsmallest(len(a), iterable=a)}')

    print(f'Min Heap result for a with key b: {min_heap(iterable=a, key=b.get)}')
    print(f'Min Heap from heapq library result for a with key b: {pq.nsmallest(len(a), iterable=a, key=b.get)}')