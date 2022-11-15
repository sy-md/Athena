package main

import "fmt"


type node struct {
	data string
	lf *node
	rt *node
}


func main() {
	root := node{data: "king"}
	root.lf = &node{data: "queen"}
	root.rt = &node{data: "prince"}

	fmt.Println(root.data)
	fmt.Println(root.lf.data)
	fmt.Println(root.rt.data)
}
