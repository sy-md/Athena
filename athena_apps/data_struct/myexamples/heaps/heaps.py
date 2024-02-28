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
        
        """


        if self.size == 1:
            return WithoutLibraryHeap.display(self)
        
        cnt = self.size -1
        while self.storage[cnt -1] > self.storage[cnt]:
            if cnt <= 0:
                break
            if self.storage[cnt] < self.storage[cnt -1]:
                self.storage[cnt], self.storage[cnt -1] = self.storage[cnt-1], self.storage[cnt]
            cnt -= 1


            print("heapify",self.storage)
            print("cnt-1",self.storage[cnt-1]) # 7
            print("cnt-2",self.storage[cnt-2]) # 10

        #return WithoutLibraryHeap.display(self)
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
    arr = [3,5,1,2,6,8,7]

    for i in arr:
        tr2.insert(i)

    # assert that [1, 2, 3, 5, 6, 8, 7] is the correct heap agasint my finshed implementation
    print(f"tr2 storage: {tr2.storage}")
    print(f"the heapq answer: {heapq.heapify(tr2.storage)}" )
    assert (tr2.storage == heapq.heapify(tr2.storage)), "the heap is not correct"

    #tr2.insert(100)
    #tr2.insert(230)
    #tr2.insert(44)
    #tr2.insert(1)
    #tr2.insert(74)
    #tr2.insert(17)
    #tr2.insert(5)
    #tr2.insert(80)
    #tr2.insert(90)
    #tr2.insert(100)
    #tr2.insert(110)
    print("running the display method:")
    tr2.display()
