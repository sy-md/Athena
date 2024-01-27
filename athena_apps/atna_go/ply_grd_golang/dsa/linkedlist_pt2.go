package main

import (
	f "fmt"
)

type node struct { // my nodes [1,[2,[...]]]
	data int
	nx   *node
}
type linkedlist struct{ head *node }

func (l *linkedlist) insert(num int) { // inserting node at end of linkedlist
	nd := &node{data: num} //create a node
	cur := l.head          //currenet node

	if l.head == nil { //if no head make a head
		l.head = nd
	} else {
		for cur.nx != nil { //find the next avaiable spot for the node
			cur = cur.nx //ever node go to your next node
		}
		cur.nx = nd //makes last nodes next the new node
	}
}

func (l *linkedlist) add_end(val int) { // adding a node at the end of a linkedlist
	nd := &node{ //make the node
		data: val,
	}
	cur := l.head // repersent the first node
	nd.nx = cur   // make the new node the new head
	l.head = nd   // then ofically make the new node the head

	f.Printf("\nheads next before: %v", l.head.nx.data)     //1
	f.Printf("\nadd new node at head: %v \n", l.head.data)  //4
	f.Printf("heads new next after: %v \n", l.head.nx.data) //1

}

func (l *linkedlist) display() { // displaying the linkedlist
	cur := l.head //current node

	for cur.nx != nil {
		f.Printf("%v -->", cur.data)
		cur = cur.nx
	}
	f.Printf("%v -->end", cur.data)
}

func main() {
	ll := linkedlist{}
	ll.insert(1)
	ll.insert(2)
	ll.insert(3)
	ll.display() // 1,2,3
	ll.add_end(4)
	ll.display() // 4,1,2,3
}
