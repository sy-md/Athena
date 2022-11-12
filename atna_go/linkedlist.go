type Node struct {
	data interface{}
	nx   *Node
}

type mylist struct {
	head *Node
}

func (l *mylist) insert(val int) {
	nd := &Node{data: val} // make node
	p := l.head            //var for head

	if l.head == nil { // check if head is nil
		l.head = nd
	} else { // if not nil
		for p.nx != nil {
			p = p.nx
		}
		p.nx = nd
	}
}

func main() {
	kk := mylist{}
	kk.insert(1)
	kk.insert(2)
	kk.insert(3)
	f.Printf("%v", kk.head.data)
	f.Printf("%v", kk.head.nx.data)
	f.Printf("%v", kk.head.nx.nx.data)
}