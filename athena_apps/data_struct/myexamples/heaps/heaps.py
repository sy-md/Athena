"""
practicing the heap data structure

without the python library and with the python library


going to use two clsaaes to implement the heap data structure
1. using the python library
2. without using the python library

so i minheap

"""

import heapq
import json
from typing import Optional

class WithLibraryHeapq:
    pass

class WithoutLibraryHeap:
    def __init__(self, capacity=10) -> None:
        self.storage = [] # list to store the elements of the heap
        self.capacity = capacity # maximum number of elements the heap can hold
        self.size = 0 # number of actually elements in the heap

    def is_min_heap(self, arr) -> bool:
        """
        given the array of elements, check if the array is a min heap
        the while loop is used to check if the left and right child of the current
        """
        cur = 0
        left_child = 2*cur + 1
        right_child = 2*cur + 2

        while cur < len(arr):
            """
            
            """
            if left_child < len(arr) and arr[cur] < arr[left_child]:
                return True
            if right_child < len(arr) and arr[cur] < arr[right_child]:
                return True
            cur += 1
            left_child = 2*cur + 1
            right_child = 2*cur + 2

    def insert(self, value):
        if self.size == self.capacity:
            WithoutLibraryHeap.display(self)
        else:
            self.storage.append(value)
            self.size += 1
            print(f"inserted {value} into the heap")
            print(f"before heapify {self.storage}")
            WithoutLibraryHeap.heapify(self)

    def heapify(self): # bubble up the newly added node to the correct position
        """
        cur is the index of the current node
        the parent of the node at index i is at index (cur-1)//2
        the left child of the node at index i is at index 2*cur + 1
        the right child of the node at index i is at index 2*cur + 2

        this method is used to bubble up the newly added node based on thee currnet
        node and its parent node then swap the nodes if the current node is less than
        its parent node.
        """
        if self.size == 1: # if the heap is only one element
            return WithoutLibraryHeap.display(self)

        cur = self.size - 1
        while cur > 0 and self.storage[cur] <= self.storage[(cur-1)//2]:
            self.storage[cur], self.storage[(cur-1)//2] = self.storage[(cur-1)//2], self.storage[cur]
            cur = (cur-1)//2
            print("heapify",self.storage)

        WithoutLibraryHeap.display(self)

    def display(self):
        payload = {
            "storage": self.storage,
            "capacity": self.capacity,
            "size": self.size,
            "error": "the heap is not out of capacity"
        }
        json_file = "./heaps.json"
        if self.size >= self.capacity:
            payload["error"] = "the heaps capacity full"
        with open(json_file, "w") as myfile:
            json.dump(payload, myfile)



if __name__ == "__main__":
    #watch -d -n 2 batcat heaps.json
    tr1 = WithLibraryHeapq()
    tr2 = WithoutLibraryHeap()

    #arr = [17,15,12,10,7,6,5]
    #5, 6, 7, 10, 12, 15, 17
    #arr = [3,5,1,2,6,8,7]
    arr = [100,70,50,125,45,60,10]

    for i in arr:
        tr2.insert(i)
    
    if tr2.is_min_heap(arr):
        print("the array is a min heap")
    else:
        print("the array is not a min heap")


    # assert that [1, 2, 3, 5, 6, 8, 7] is the correct heap agasint my finshed implementation

    #tr2.insert(100)
    #tr2.insert(230)
    #tr2.insert(44)
    #tr2.insert(74)
    #tr2.insert(1)
    #tr2.insert(17)
    #tr2.insert(5)
    #tr2.insert(80)
    #tr2.insert(90)
    #tr2.insert(100)
    #tr2.insert(110)
    print("running the display method:")
    tr2.display()
