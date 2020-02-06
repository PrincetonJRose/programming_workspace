package main

import "fmt"

func main() {
	fmt.Printf("hello, world\n")
	var truthy = sayGreeting(myAge, myGreeting)
	fmt.Println(truthy)
}

var myAge int = 35
var myGreeting string = "Hello there!"

func sayGreeting(age int, greeting string) bool {
	fmt.Println("This is your age:", age)
	fmt.Println("This is your greeting message: " + greeting)
	return true
}
