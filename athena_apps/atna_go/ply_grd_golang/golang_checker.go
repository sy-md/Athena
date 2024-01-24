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
/*

this function adds a list of people to the db

*/
func (d *BarDB) add(list_of_people []Person) {

	var seen = make(map[Person]bool)

	for x := range list_of_people {
		if seen[list_of_people[x]] == false { // if name is not db
			d.id = append(d.id, list_of_people[x])
			seen[list_of_people[x]] = true // seen
			f.Println(d.id)
		} else {
			f.Printf("this name %v is already in the db", list_of_people[x])
		}
	}
}

func main() {
	p1 := Person{Name: "marell"}
	p2 := Person{Name: "tilly"}
	p3 := Person{Name: "marell"}
	people := []Person{p1, p2, p3}
	mydb := BarDB{}
	mydb.add(people)
}
