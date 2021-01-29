##Configure January Expenses and LIST##
January_Automotive_Expenses = int(100)
January_Miscellaneous_Expenses = int(100)
January_Expenses = [
    'January_Automotive_Expenses', January_Automotive_Expenses,
    'January_Miscellaneous_Expenses', January_Miscellaneous_Expenses
]

##Configure February Expenses and LIST##
February_Automotive_Expenses = int(100)
February_Miscellaneous_Expenses = int(100)
February_Expenses = [
    'February_Automotive_Expenses', February_Automotive_Expenses,
    'February_Miscellaneous_Expenses', February_Miscellaneous_Expenses
]

##Configure January Income and LIST##
January_Primary_Income = int(100)
January_Other_Income = int(100)
January_Income = [
    'January Primary Income', January_Primary_Income,
    'January Other Income', January_Other_Income
]

##Configure February Income and LIST##
February_Primary_Income = int(100)
February_Other_Income = int(100)
February_Income = [
    'February Primary Income', February_Primary_Income,
    'February Other Income', February_Other_Income
]
####################################################################################
##Call to specific month and category function##
def Selection(Month,Category,Monthly_Expense_Categories):
    while True:
        if Month == 'January' and Category == 'Expenses' and Monthly_Expense_Categories == 'All':
            print(January_Expenses)
        elif Month == 'January' and Category =='Expenses' and Monthly_Expense_Categories == 'Automotive Expenses':
            print('January Automotive Expenses - $',January_Automotive_Expenses)
        elif Month == 'January' and Category == 'Expenses' and Monthly_Expense_Categories == 'Miscellaneous Expenses':
            print('January Miscellaneous Expenses - $',January_Miscellaneous_Expenses)
        elif Month == 'January' and Category == 'Income' and Monthly_Expense_Categories == 'All':
            print(January_Income)
        elif Month == 'January' and Category == 'Income' and Monthly_Expense_Categories == 'Primary Income':
            print('January Primary Income - $',January_Primary_Income)
        elif Month == 'January' and Category == 'Income' and Monthly_Expense_Categories == 'Primary Income':
            print('January Primary Income - $',January_Primary_Income)
        elif Month == 'February' and Category == 'Expenses' and Monthly_Expense_Categories == 'All':
            print(February_Expenses)
        elif Month == 'February' and Category == 'Expenses' and Monthly_Expense_Categories == 'Automotive Expenses':
            print('February Automotive Expenses - $',February_Automotive_Expenses)
        elif Month == 'February' and Category == 'Expenses' and Monthly_Expense_Categories == 'Miscellaneous Expenses':
            print('February Miscellaneous Expenses - $',February_Miscellaneous_Expenses)
        elif Month == 'February' and Category == 'Income' and Monthly_Expense_Categories == 'All':
            print(February_Income)
        else:
            print("NOT CORRECT")
        break

##Questions for def Selection(Month,Category) Function##
Month=input("What Month:")
Category=input("Which Accounting Category:")
Monthly_Expense_Categories=input("Specify:")
Selection(Month,Category,Monthly_Expense_Categories)


