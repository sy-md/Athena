package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    //json file
    json1 := `{"martell": "54321","terry": "12345"}`
    //struct mock up to assces it
    obj := map[string]interface{}{}
    //unmarshal
    json.Unmarshal([]byte(json1), &obj)

    //before
    fmt.Println(obj)


    if _, there := obj["terry"]; there {
        fmt.Println(obj["terry"])
        //wanna change it... ok jellypop
        obj["terry"] = "jellypop"
    }
    old_psw := obj["martell"]
    fmt.Println("saving old password")
    delete(obj, "martell")
    obj["crazymartrll"] = old_psw
    
    //update key
    //obj["key2"] = obj["key1"]
    //delete(obj, "key1")
    //update val
    //obj["key2"] = "terry"
    //delete(obj, "value1")

    fmt.Println(obj) // <-- map[key2:value1]
}
