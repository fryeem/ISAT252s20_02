for x in range(100):
    if x%15 == 0 and x !=0:
        print("Fizzbuzz")
    elif x%5 == 0 and x !=0:
        print("buzz")
    elif x%3 == 0 and x !=0:
        print("Fizz")
    else:
        print(x)