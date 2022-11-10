package main

import (
	"fmt"
	"os/exec"
	//"log"
)

/*
1.) wlaking a folder and recursively counting
2.) put into json
3.) display and choose number to veiew
*/
const file = "'Pawg vs. BBC-Lp87T8aZ4Gr.mp4'"

type myVideo struct {
	Id     int    `json:"id"`
	Name   string `json:"video"`
	Mytype string `json:"text"`
}

func main() {

	test := myVideo{
		Id:     1,
		Name:   file,
		Mytype: "really loke this one",
	}

	cmd, err := exec.Command("ranger").Output()
	if err != nil {
		fmt.Println(err)
	}
	output := string(cmd[:])
	//fmt.Printf("%s",cmd)
	fmt.Println(test)
	fmt.Println(output)


}
