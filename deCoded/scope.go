package main

import "fmt"

func main() {
	var1 := 5
	func some_func(){
		var2 := 6
		fmt.Println(var2)

		func some_inner_function(){
			var3 := 7
			fmt.Println(var1)
			fmt.Println(var2)
			fmt.Println(var3)
		}
		some_func()
		
	}
		some_inner_function()
	
}