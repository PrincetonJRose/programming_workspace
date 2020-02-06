package main

import (
	"fmt"

	"github.com/d4l3k/go-pry/pry"
)

var age int = 35
var greeting = "Oh man," + " Go is pretty crazy!"

func main() {
	fmt.Println("Hello, World!")
	if age > 30 {
		fmt.Println("Boy, you're really old @ %i .", age)
	} else {
		fmt.Println(age)
	}
	sayGreeting()
	pry.Pry()
}

func sayGreeting() {
	fmt.Println("This is the greeting:\n" + greeting + "\nAnd this is strings in a nutshell")
}
