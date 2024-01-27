package main
import "fmt"

type kids struct {
	name string
	toy string
}

func (self *kids) who() {
	fmt.Println("my name is",self.name,"and my fav toy is",self.toy)
}
type house struct {
	lname string
	kd_fn string
	kd_ty string
}

func (self *house) family()  {
	mydict := map[string]map[string]string{}
	mydict[self.lname] = map[string]string{}
	mydict[self.lname][self.kd_fn] = self.kd_ty
	fmt.Println(mydict)
}
func main() {
	kd1 := kids{name: "jarry",toy: "plane"}
	kd2 := kids{name: "harry",toy:"car"}

    //family 1
	hood := house{lname: "dorsett",kd_fn: kd1.name, kd_ty: kd1.toy}
    hood.family()
    kd1.who()

    //family 2
	hood2 := house{lname: "hodes",kd_fn: kd2.name, kd_ty: kd2.toy}
    hood2.family()
    kd2.who()
}
