# go coding

`package main

import (fmt)
`
> error check out pkg

# if statments
`fmt.Println()

if x > 5 {
    fmt.Println("sup")
} elif x < 5  {
    fmt.Println("nope")
}
`
# List
`
a := [5]int{3,5,7,6,8} | empty == [0,0,0,0,0]

x := []int{1,2}
x.append(x,3)
`
# Dict 
`
mydict := make(map[string]int)

mydict["jarry"] = 6
delete(mydict, key)
`

# loops for/ while

`
for i,v := range a{
    //for loop in list or dict
}

for i := 0; i<5; ; i++ {
    print
}
`
##  while loop
`
i := 0 

for i < 5 {
    print
    i++
}
`
# classes
`
type person struct {
    name string
    age int
}
func (j *person) speak() string {
    //return or text or whatever
}

\\when you use the driver code
p := person{name: "",age: 0}
p1 := person{name: "",age: 0}
`
# pointers 
`
    i := 1
    i > 1
    &i >> address of i
`
#I/O

`
package main
import "fmt"

func main() {
    var i int

    fmt.Print("type number: ")
    fmt.Scan(&i)
    fmt.Println(""your number is:" ,i)
}
`
