/*linked list 22:10 - 22:15*/
package main

import ( 
	f "fmt" 
)

type Node struct {
	data string
	nx *Node

}

type linkedlist struct {
	head *Node
}

func(l *linkedlist) insert(val string) {
	nd := &Node{data: val}
	p := l.head

	if l.head == nil {
		l.head = nd
	} else {
		for p.nx != nil { // while
			p = p.nx
		}
		p.nx = nd
	}
}


func main() {
	mylst := linkedlist{}
	mylst.insert("martell")
	mylst.insert("man man")
	mylst.insert("timmy")
	mylst.insert("nared")
	f.Printf("%v \n",mylst.head.data)
	f.Printf("%v \n",mylst.head.nx.data)
	f.Printf("%v \n",mylst.head.nx.nx.data)
	f.Printf("%v \n",mylst.head.nx.nx.nx.data)
}
