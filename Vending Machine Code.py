ItemList=['1. Snickers','2. Kit Kat','3. Reecees','4. Milky Way','5. Twix']
print(ItemList[0])
print(ItemList[1])
print(ItemList[2])
print(ItemList[3])
print(ItemList[4])

Price = {
    'Snickers':1.25,
    'Kit Kat': 1.25,
    'Reesees':1.25,
    'Milky Way':1.25,
    'Twix':1.25,
}

QuantityAvailable = {
        'Snickers':10,
        'Kit Kat':10,
        'Reecees':10,
        'Milky Way':10,
        'Twix':10,
}

Item = input("Enter choice(1/2/3/4/5): ")

while True:
    if Item in ('1'):
        print('Snickers')
        print(Price['Snickers'])
        print(QuantityAvailable['Snickers'])
    elif Item in ('2'):
        print("Kit Kat")
        print(Price['Kit Kat'])
        print(QuantityAvailable['Kit Kat'])
    elif Item in ('3'):
        print("Reecees")
        print(Price['Reecees'])
        print(QuantityAvailable['Reecees'])
    elif Item in ('4'):
        print("Milky Way")
        print(Price['Milky Way'])
        print(QuantityAvailable['Milky Way'])
    elif Item in ('5'):
        print("Twix")
        print(Price['Twix'])
        print(QuantityAvailable['Twix'])
    else:
        print("INVALID SELECTION")
    break

print("COST OF QUANTITY SELECTED")
x = int(input("Quantity Desired:"))

while True:
    if Item in ('1') and x<=10:
        print(Price['Snickers']*x)
    elif Item in ('2') and x<=10:
        print(Price['Kit Kat']*x)
    elif Item in ('3') and x<=10:
        print(Price['Reecees']*x)
    elif Item in ('4') and x<=10:
        print(Price['Milky Way']*x)
    elif Item in ('5') and x<=10:
        print(Price['Twix']*x)
    else:
        print("NOT ENOUGH PRODUCT")
    break


print("Quantity Remaining")
while True:
    if Item in ('1') and x<=10:
        print(QuantityAvailable['Snickers']-x)
    elif Item in ('2') and x<=10:
        print(QuantityAvailable['Kit Kat']-x)
    elif Item in ('3') and x<=10:
        print(QuantityAvailable['Reecees']-x)
    elif Item in ('4') and x<=10:
        print(QuantityAvailable['Milky Way']-x)
    elif Item in ('5') and x<=10:
        print(QuantityAvailable['Twix']-x)
    else:
        print("NOT ENOUGH PRODUCT")
    break
