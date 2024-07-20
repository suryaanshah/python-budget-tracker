from datetime import datetime
import pandas as pd


df = pd.DataFrame(columns=["date", "amount", "type"])

def main():
    todo = input("What do want to do?\n 1. record a statement (R)\n 2. show the balance-sheet (B)\n 3. tutorial (T)\nYour Answer: ")
    if todo.upper() == 'R':
        record()
    # elif todo.upper() == 'B':
    #     balance()
    # elif todo.upper() == 'T':
    #     tutorial()
    else:
        main()

def record():
    track = input("Is it an expense (E) or an income (I)? ")

    if track.upper() == "E":
        amount = trackexpense()
        date = trackdate()
        df.loc[len(df)] = [date, amount, "expense"]
        df.to_csv("track.csv", index=False)
    elif track.upper() == "I":
        amount = trackincome()
        date = trackdate()
        df.loc[len(df)] = [date, amount, "income"]
        df.to_csv("track.csv", index=False)
    else:
        record()

def trackexpense():
    while True:
        try:
            expense = int(input("Enter the expense: "))
            return expense
        except ValueError:
            print("Not an integer, please try again.")

def trackincome():
    while True:
        try:
            income = int(input("Enter the income: "))
            return income
        except ValueError:
            print("Not an integer, please try again.")

def trackdate():
    while True:
        try:
            date_str = input("Enter the date (DD-MM-YYYY): ")
            date_object = datetime.strptime(date_str, "%d-%m-%y").date()
            return date_object
        except ValueError:
            print("Invalid Date Format, please try again.")

main()

