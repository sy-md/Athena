package main

import (
  "fmt"
  "log"
  "io/ioutil"
  "os"

  "net/http"

  "encoding/json"
  "github.com/gin-gonic/gin"
)

type Plots struct {
  Type string  `json:"type"`
  Plant string  `json:"plant"`
  Water_lvl int `json:"thirst"` 
}
type User struct {
  Id string `json:"username"`
  Psw string `json:"password"`
  Farm []Plots   `json:"myfarm"`
}

func makedb() {
  //creats file checks or err
  emptyFile, err := os.Create("emptyFile.json")
  if err != nil {
    log.Fatal(err)
  }
  //makes db encapsulate the data
  db := []User{}
  
  // encode the data --> write tye encode to json
  file, _ := json.Marshal(db)  
  _ = ioutil.WriteFile("emptyFile.json", file, 0644)

  fmt.Println("made new db",*emptyFile)
}

func makeUser(ctx *gin.Context) {
  file, err := os.Open("emptyFile.json")
  if err != nil {
        // handle the error here
    return
  }
  defer file.Close()

  usn := ctx.Param("usn")
  psw := ctx.Param("psw")

  tmp := &User{
   Id : usn,
   Psw: psw,
  }
  //endcode the data into readable json
  data, err := json.Marshal(tmp)
  if err != nil {
	  fmt.Println(err)
  }

  // send to json
  err = ioutil.WriteFile("emptyFile.json", data, 0644)
  if err != nil {
	  fmt.Println(err)
  }
  ctx.JSON(http.StatusOK, gin.H{usn:tmp})
  //c.bind
  //write to file
} 

func main() {
  var ans string
  fmt.Println("make the db? y/n")
  fmt.Scan(&ans)
  if ans != "n" {
    makedb()
  }
  router := gin.Default()
  router.LoadHTMLGlob("templates/*.html")
  router.GET("/users/:usn", makeUser) // home page
  router.POST("/create/:usn/:psw", makeUser) // home page
  router.Run(":3000")
}



