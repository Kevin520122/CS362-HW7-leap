def print_FizzBuzz():
    
    
    res = ""
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            res += "FizzBuzz "
        elif i % 3 == 0:
            res += "Fizz "
        elif i % 5 == 0:
            res += "Buzz "
        else:
            res += str(i) + " "
    print(res)
    return res
    


    
