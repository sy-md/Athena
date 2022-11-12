package main

import (
	f "fmt"
)

type Person struct {
	Name string
}

type BarDB struct {
	id     []Person
	Member []string
}

func (d *BarDB) add(list_of_people []Person) {
	var mymap = make(map[Person]bool)
	for x := range list_of_people {
		if mymap[list_of_people[x]] != true {
			mymap[list_of_people[x]] = true
			d.id = append(d.id, list_of_people[x])
			f.Println(d.id)
		}
	}
}

func main() {
	p1 := Person{Name: "marell"}
	p2 := Person{Name: "tilly"}
	p3 := Person{Name: "marell"}
	mydb := BarDB{}
	people := []Person{p1, p2, p3}
	mydb.add(people)
}
