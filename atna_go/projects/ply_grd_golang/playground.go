package main 

import (
    f "fmt"
    "errors"
)

/*
wanna see if creating a interface for 
the choosing of which function to will 
work instead running all of then
*/

func main() { 
    keepTrack()
    panicRecover()

    err := myStore("martell",int(18))
    if err != nil {
        f.Println(err)
    }

    mycont := container{data: []int{1,2,3,4,5}}
    mycont.noptr(8) 
    mycont.withptr(8)

}

/****************************************/
func keepTrack() {
    ls := []int{1,4,6,8,11,14,17}
    var tmp []int //caught 
    var ans int = 2 //anchor

    //f.Print("type a number") // 2
    //f.Scan(&ans)

    defer func() {
        if r := recover(); r != nil {
            f.Println("answer is:",tmp)
        }
    }()

    i,j := 0,1
    for { // while loop
        t := ls[i] + ans
        if t != ls[j] && j >= len(ls) {
            panic("out side of index")
        } else if t == ls[j]{
            tmp = append(tmp, ls[j])
        }    
        i++
        j++
    }
}
/****************************************/
func panicRecover() {
    defer func() {
        /*
        {PYTHON}
        if (r is true) and (r != None):
            print("working on a fix")
        */
        if r := recover(); r != nil {
            f.Println("working on a fix")
        }
    }() // dont forget me
    v := 1
    if v != 2 {
        panic("oh shit")
    }
}
/****************************************/
/*
funcation output8ng a error with the package using speical
errors returnis 
*/
type person struct {
    name string
    age int
}
func myStore(name string, age int) error {
    if name == "" {
        return errors.New("need a name")
    }
    if age < 21 {
        return errors.New("not old enough")
    }
    return nil
}
/****************************************/
/*
pointer with recviers vs no pointer with reciver
*/

type container struct {
    data []int
}

func(t container) noptr(n int) { //copy of and manipulation

    t.data = append(t.data, n)
    f.Printf("with no pointer: %v \n",t.data)
}
func(t *container) withptr(n int) { //manipulation

    t.data = append(t.data, n)
    f.Printf("with pointer: %v",t.data)
}
