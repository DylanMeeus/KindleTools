package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"reflect"
)

type BookHighlights map[string][]string

func main() {
	fileLocation := os.Args[1]
	hl, err := highlights(fileLocation)
	if err != nil {
		fmt.Printf("something went wrong: %v\n", err)
		os.Exit(1)
	}
	entry := randomEntry(hl)
	fmt.Printf("%v\n", entry)
}

// randomEntry prints a random highlight and the book that it's highlighted in
func randomEntry(b BookHighlights) string {
	nbooks := len(b)
	r := rand.Intn(nbooks)
	keys := reflect.ValueOf(b).MapKeys()

	value := keys[r].Interface()
	hls := b[value.(string)]
	r = rand.Intn(len(hls))
	hl := hls[r]
	return fmt.Sprintf("%v ~ %v\n", hl, value)
}

// highlights parses the json file and stores the entries in the BookHighlights
func highlights(file string) (BookHighlights, error) {
	x, err := ioutil.ReadFile(file)
	if err != nil {
		return nil, err
	}
	var m BookHighlights
	err = json.Unmarshal(x, &m)
	if err != nil {
		return nil, err
	}
	return m, nil
}
