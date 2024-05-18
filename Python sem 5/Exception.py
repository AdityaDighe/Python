class baseerror(Exception):
    pass

class highvalueerror(Exception):
    pass

class lowvalueerror(Exception):
    pass

value = 29


while(1):
    try:
        x=int(input("Enter a number: "))
        if x>value:
            raise highvalueerror

        if x<value:
            raise lowvalueerror
    
    except lowvalueerror:
        print("Value too low, try again")

    except highvalueerror:
        print("Value too high, try again")

    else:
        print("Correct Answer")
        break

