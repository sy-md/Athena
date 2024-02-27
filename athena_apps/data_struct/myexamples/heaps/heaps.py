"""
practicing the heap data structure

without the python library and with the python library


going to use two clsaaes to implement the heap data structure
1. using the python library
2. without using the python library

so i minheap

"""

import json
from typing import Optional

class WithLibraryHeapq:
    pass

class WithoutLibraryHeap:
    def __init__(self, capacity=10) -> None:
        self.storage = [0] * capacity # list to store the elements of the heap
        self.capacity = capacity # maximum number of elements the heap can hold
        self.size = 0 # number of actually elements in the heap

    def insert(self, value):
        if self.size == 0:
            self.storage[self.size] = value
            self.size += 1
            print(f"inserted {value} into the heap")
            print("before heapify",self.storage)

        else: 
            if self.size < self.capacity: # meaning the heap is not empty
                # insert the value at the next available index
                #then increase the size of the heap
                self.storage[self.size] = value
                self.size += 1
                print(f"inserted {value} into the heap size is{self.size}")
                print("before heapify",self.storage)
                return WithoutLibraryHeap.heapify(self) 

    def heapify(self):
        """
            heapify mean when run this method,
            the heap will be put  in the correct order
        """
        #if self.storage[self.size] == 1:
        #else:
        #grab the last added node and check for if smaller the cur root
        cnt = self.size
        root = self.storage[0]
        while root >= self.storage[cnt-1]:
            if cnt <= 0:
                break
            if self.storage[cnt-1] < self.storage[cnt -2]:
                self.storage[cnt-1], self.storage[cnt -2] = self.storage[cnt-2], self.storage[cnt-1]
            cnt -= 1


            print("heapify",self.storage)
            print("cnt-1",self.storage[cnt-1]) # 7
            print("cnt-2",self.storage[cnt-2]) # 10

        return WithoutLibraryHeap.display(self)
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
            db = json.dump(payload, myfile)
            #print(db)



if __name__ == "__main__":
    #watch -d -n 2 batcat heaps.json
    tr1 = WithLibraryHeapq()
    tr2 = WithoutLibraryHeap()

    tr2.insert(7)
    tr2.insert(15)
    tr2.insert(10)
    tr2.insert(12)
    tr2.insert(6)
    tr2.insert(17)
    tr2.insert(5)
    #tr2.insert(80)
    #tr2.insert(90)
    #tr2.insert(100)
    #tr2.insert(110)
    print("running the display method:")
    tr2.display()
