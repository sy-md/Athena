package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"net/http"

	"encoding/json"

	"github.com/gin-gonic/gin"
)

const myfile = "grd_db.json"

type User struct {
	Name    string `json:"username"`
	Pswd    string `json:"password"`
	Email   string `json:"email"`
	Storage []byte `json:"file_strg"`
}
type getFiles struct{ file string }

//type getFiles struct{ file string }

func resetDb() { // just reset the db
	emptyFile, err := os.Create(myfile)
	if err != nil {
		log.Fatal(err)
	}
	//makes db encapsulate the data
	db := [][]User{}

	// encode the data --> write tye encode to json
	file, _ := json.Marshal(db)
	_ = ioutil.WriteFile(myfile, file, 0644)
	fmt.Println("made new db", *emptyFile)
}
func signUp(ctx *gin.Context) {
	file, err := os.Open(myfile)
	if err != nil { // handle the error here
		return
	}
	defer file.Close()

	psw := ctx.Param("psw")
	usn := ctx.Param("usn")
	emal := ctx.Param("emal")

	tmp := &User{
		Name:  usn,
		Pswd:  psw,
		Email: emal,
	}

	//endcode the data into readable json
	data, err := json.Marshal(tmp)
	if err != nil {
		fmt.Println(err)
	}

	// send to json
	err = ioutil.WriteFile(myfile, data, 0644)
	if err != nil {
		fmt.Println(err)
	}
	ctx.JSON(http.StatusOK, gin.H{usn: tmp})
}
func logIn(ctx *gin.Context) { //if the creditnals are good welcome {grUpload}
	// open the db

	//check if name and passwd is there
	psw := ctx.Param("psw")
	usn := ctx.Param("usn")

	//if passwd and name match then show data - redirect to grUpload
	ctx.JSON(http.StatusOK, gin.H{usn: psw})
}
func grUpload(ctx *gin.Context) {} //put the image in a q {hashing}
func hashing(ctx *gin.Context)  {} // hasing for sercuity [psw,tokn,email]

func index(c *gin.Context) {
	c.HTML(http.StatusOK, "index.html", gin.H{
		"title": "main start",
	})
}

func main() {
	var ans string
	fmt.Println("make the db? y/n")
	fmt.Scan(&ans)
	if ans != "n" {
		resetDb()
	}

	router := gin.Default()
	router.LoadHTMLGlob("templates/*")
	router.POST("/create/:usn/:psw/:emal", signUp) // home page
	router.GET("/:usn/:psw", logIn)                // home page
	router.GET("/upload", grUpload)                // home page
	router.GET("/index", index)
	router.Run(":3000")
}
