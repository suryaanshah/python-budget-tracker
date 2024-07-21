from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser


df = pd.DataFrame(columns=["date", "expense", "income", "balance"])

def main():
    todo = input("What do want to do?\n 1. record a statement (R)\n 2. show the balance-sheet (B)\n 3. tutorial (T)\n 4. Exit (E)\nYour Answer: ")
    if todo.upper() == 'R':
        record()
    elif todo.upper() == 'B':
        balance()
    elif todo.upper() == 'T':
         tutorial()
    elif todo.upper() == 'E':
        return 0
    else:
        main()

def record():
    track = input("Is it an expense (E) or an income (I)? ")

    if track.upper() == "E":
        expense = trackexpense()
        date = trackdate()
        df.loc[len(df)] = [date, expense, 0, -expense]
        df.to_csv("track.csv", index=False)
        main()
    elif track.upper() == "I":
        income = trackincome()
        date = trackdate()
        df.loc[len(df)] = [date, 0, income, income]
        df.to_csv("track.csv", index=False)
        main()
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
            date_str = input("Enter the date (DD-MM-YY): ")
            date_object = datetime.strptime(date_str, "%d-%m-%y").date()
            return date_object
        except ValueError:
            print("Invalid Date Format, please try again.")


def balance():
    balance = df["balance"].cumsum()
    netbalance = df["balance"].sum()
    print(f"\nYour net balance is {netbalance}\n")
    plt.plot(df["date"],balance)
    plt.title("Balance every day")
    plt.xlabel("Date")
    plt.ylabel("Balance")
    plt.savefig("balance-graph.png")
    main()


def tutorial():
    print("here is a sample use case video....")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    main()


main()

