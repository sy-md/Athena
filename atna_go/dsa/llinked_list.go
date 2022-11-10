package main

import ("fmt")

type node struct {
	data int
	next *node 
}

type linked struct {
	head *node 
}

func (ln *linked) insert(n node){
	cur := ln.head

	if cur == nil { 
		cur = &n
	}

	for cur.next != nil {
		cur = cur.next
	}
	cur.next = &n	
}

func (l *linked) display() {
	ptr := l.head

	for ptr != nil {
		fmt.Printf("%v ->", ptr.data)
		ptr = ptr.next
	}
	fmt.Println("end")
}

func main() {
	mylst := linked{} 

	dum := node{data: 0}
	nd1 := node{data: 1} 
	nd2 := node{data: 2} 
	nd3 := node{data: 3} 

	mylst.head = &dum
	mylst.insert(nd1)
	mylst.insert(nd2)
	mylst.insert(nd3)

	mylst.display() 

}
