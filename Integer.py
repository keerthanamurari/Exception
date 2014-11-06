from random import randrange
 
print("Integer Divisions")
 
while(True):
    a=randrange(5)
    b=randrange(5)
    print(" ")   
    if(a%2 != 0):
        a=a+1
 
    try:
        print("what's the value of :" ,int(a),"/",int(b))
        result = int(a)/int(b)
        print(int(result))
        userinput = input("Please enter the number: ")
        if(int(userinput) == int(result)):
            print("Correct!")
        else:
            print("Incorrect!")
    except ValueError:
        print("Please enter integers only")
    except ZeroDivisionError:
        print("Can't be divided by zero")
    except Exception as e:
        print("Unknown error")
 
