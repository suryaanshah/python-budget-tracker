
"""
What it does:
1. help you track: expenses (E), income (I)
2. generates your balance sheet
3. ask your assets: what do you own
4. ask your liabilities: obligation to someone else
5. tell your equity/net-worth: A=L+E
"""

track=input("Is it an expense (E) or an income (I)? ");

if track == "E":
    expense=int(input("please enter the amount of expense: "));
    date=input("Please enter the date: ");


