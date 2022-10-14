for x in range(0 , 101):
    if x % 3 == 0 and x % 5 != 0:
        print("fizz " , end=" ")
    elif x % 5 == 0 and x % 3 != 0:
        print("buzz ", end=" ")
    elif x % 5 == 0 and x % 3 == 0:
        print("fizzbuzz ", end=" ")
    else:
        print(x , end=" ")

    x= x+1
