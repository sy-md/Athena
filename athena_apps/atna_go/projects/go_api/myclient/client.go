package main

import (
    curl "github.com/andelf/go-curl"
)

func main() {
    easy := curl.EasyInit()
    defer easy.Cleanup()
    if easy != nil {
        easy.Setopt(curl.OPT_URL, "http://localhost:8080/user/kelly/farm")
        easy.Perform()
    }
}


//unc main() {
//       easy := curl
//        easy := curl.EasyInit() 
//        defer easy.Cleanup() 
//        if easy != nil { 
//                easy.Setopt(curl.OPT_URL, "http://localhost:8080/user/kelly") 
//                easy.Perform() 
//        } 
//}
