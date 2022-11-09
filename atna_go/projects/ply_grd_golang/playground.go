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

}

/****************************************/
func keepTrack() {
    ls := []int{1,4,6,8,11,14,17}
    var tmp []int //caught 
    var ans int = 2 //anchor

 /   //f.Print("type a number") // 2
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
type person struct {
    name string
    age int
}
/*
funcation output8ng a error with the package using speical
errors returnis 
*/
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
