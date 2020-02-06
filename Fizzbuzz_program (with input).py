def fizzbuzz_program (number): ###defines new program called fizzbuzz_program with parameter "number"
    for x in range(number):
        if x%15 == 0 and x !=0:
            print("fizzbuzz")
        elif x%3 == 0 and x !=0:
            print ("fizz")
        elif x%5 == 0 and x !=0:
            print("buzz")
        else:
            print(x)

y=int(input("Number for program?:")) ###asks for number and stores in variable y
fizzbuzz_program(y+1) ###puts y into program fizzbuzz_program 