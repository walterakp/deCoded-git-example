package main

import "fmt"

func hello(first string, age int) {
	fmt.Printf("Hello %s, you are %v years old", first, age)
}

func main() {
	hello("Walter", 27)
}