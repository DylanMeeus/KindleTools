package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
)

func main() {
	fmt.Println("hello world")
	x, err := ioutil.ReadFile("highlights.json")
	if err != nil {
		panic(err)
	}
	m := map[string][]string{}
	err = json.Unmarshal(x, &m)
	if err != nil {
		panic(err)
	}
	for _, v := range m {
		fmt.Printf("%v\n", v)
	}
}
