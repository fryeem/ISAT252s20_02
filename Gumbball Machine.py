ItemList=['1. Snickers','2. Kit Kat','3. Reecees','4. Milky Way','5. Twix']

Price = {
    '1. Snickers':1.25,
    '2. Kit Kat': 1.25,
    '3. Reesees':1.25,
    '4. Milky Way':1.25,
    '5. Twix':1.25,
}

QuantityAvailable = {
        '1. Snickers':10,
        '2. Kit Kat':10,
        '3. Reecees':10,
        '4. Milky Way':10,
        '5. Twix':10,
}

print("Hello!")
print("Welcome to Virtual Vending")

answer1=input("Would you like to make a purchase? (Y/N):")

def yes_no(answer1):
        while True:
                if answer1 == "Y":
                        print("What would you like to purchase?:")
                        print(ItemList[0])
                        print(ItemList[1])
                        print(ItemList[2])
                        print(ItemList[3])
                        print(ItemList[4])
                        answer2=input("Enter Choice(1/2/3/4/5):") 
                elif answer1 == "N":
                        print("Invalid Selection/Goodbye")
                        answer2='0'
                else:
                        print("Invalid Selection/Goodbye")
                        answer2='0'
                break
        return answer2
answer2 = yes_no(answer1)

def selection(answer2):
    while True:
        if answer2 in ('1'):
            print("Snickers")
            print(Price['1. Snickers'])
            print(QuantityAvailable['1. Snickers'])
        elif answer2 in ('2'):
            print("Kit Kat")
            print(Price['2. Kit Kat'])
            print(QuantityAvailable['2. Kit Kat'])
        elif answer2 in ('3'):
            print("Reecees")
            print(Price['3. Reecees'])
            print(QuantityAvailable['3. Reecees'])
        elif answer2 in ('4'):
            print("Milky Way")
            print(Price['4. Milky Way'])
            print(QuantityAvailable['4. Milky Way'])
        elif answer2 in ('5'):
            print("Twix")
            print(Price['5. Twix'])
            print(QuantityAvailable['5. Twix'])
        elif answer2 in ('0'):
            print("Invalid Selection/Goodbye")
        else:
            print("Invalid Selection/Goodbye")
        break
selection(answer2)




                



