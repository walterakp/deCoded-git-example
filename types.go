package main

import (
	"fmt"
)

func main(){
	//STRING 
	nickName := "Mr Baclava"

	//INTEGER
	var moneyInChecking int64
	moneyInChecking = 14

	//FLOAT
	moneyInSavings := 3.5

	//BOOLEAN
	amIBroke := true

	fmt.Printf("%T\n", nickName)
	fmt.Printf("%T\n", moneyInChecking)
	fmt.Printf("%T\n", moneyInSavings)
	fmt.Printf("%T\n", amIBroke)
	
}