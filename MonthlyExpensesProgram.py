##Primary Input Questions##
Month=input("What Month:")
Category=input("Which Accounting Category:")

##Arithmetic Operation using Addition## **ADD OTHER OPERATIONS**
def total(num1,num2,num3,num4,num5):
    return (num1 + num2 + num3 + num4 + num5)

##Setup monthly income lists and operations##
January_Income_List = [
        'January - Paycheck/Salary',
        'January - Other Income',
        'January - ATM Deposits',
        'January - Transfers',
        'January - Reimbursements']

##Setup monthly expense lists and operations##    
January_Expense_List = [
    'January_Automotive_Expenses',
    'January Miscellaneous Expenses',
    'January Food Expenses',
    'January Medical Expenses',
    'January Clothing Expenses'
    ]

##Setup monthly income lists and operations##
if Month == 'January' and Category == 'Income':

    ##Input configuration for Monthly Income##
    January_Primary_Income = float(input("January Primary Income:"))
    January_Other_Income = float(input("January Other Income:"))
    January_ATM_Deposits = float(input("January ATM Deposits:"))
    January_Transfers = float(input("January Transfers:"))
    January_Reimbursements = float(input("January Reimbursements:"))

    ##Arithmetic Operations##
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    operation = input("Enter operation(1/2/3/4): ")

##What to do if "January Expense"##
if Month == 'January' and Category == 'Expenses':
    
    ##Input Configuration for Monthly Expenses##
    January_Automotive_Expenses = float(input("January Automotive Expenses:"))
    January_Miscellaneous_Expenses = float(input("January Miscellaneous Expenses:"))
    January_Food_Expenses = float(input("January Food Expenses:"))
    January_Medical_Expenses = float(input("January Medical Expenses:"))
    January_Clothing_Expenses = float(input("January Clothing Expenses:"))

    ##Arithmetic Operations##
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    operation = input("Enter operation(1/2/3/4): ")
    
###Calculation setup using Month/Category/Operation##
while True:
    if Month == 'January' and Category == 'Income' and operation in ('1', '2', '3', '4'):
        num1 = January_Primary_Income
        num2 = January_Other_Income
        num3 = January_ATM_Deposits
        num4 = January_Transfers
        num5 = January_Reimbursements
    elif Month == 'January' and Category == 'Expenses' and operation in ('1', '2', '3', '4'):
        num1 = January_Automotive_Expenses
        num2 = January_Miscellaneous_Expenses   
        num3 = January_Food_Expenses
        num4 = January_Medical_Expenses
        num5 = January_Clothing_Expenses
    if operation == '1':
        print(num1, "+", num2, "+", num3, "+", num4, "+", num5, "=", total(num1, num2, num3, num4, num5))
    break
else:
    print("Invalid Input")





    





