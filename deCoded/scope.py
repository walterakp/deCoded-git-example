var1 = 5

def some_func():
    var2 = 6
   
    print(var2)
    
    def some_inner_function():
        var3 = 7
        print(var3)

    some_inner_function()

some_func()
