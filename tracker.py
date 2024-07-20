from datetime import datetime
import pandas as pd
import csv





def main():
    todo=input("What do want to do?\n 1. record a statement (R)\n 2. show the balance-sheet (B)\n 3. tutorial (T)\nYour Answer: ")
    if todo.upper()=='R':
        record()

    # elif todo.upper()=='B':
    #     balance()
    # elif todo.upper()=='T':
    #     tutorial()

    else:
        main()


def record():

    track=input("Is it an expense (E) or an income (I)? ")

    if track.upper() == "E":
        trackexpense()
        trackdate()

    elif track.upper() == "I":
        trackincome()
        trackdate()

    else:
        record()


#def balance():



def trackexpense():
    try:
        expense=int(input("enter the expense: "))
    except ValueError:
        print("Not an integer")
        trackexpense()


def trackincome():
    try:
        income=int(input("enter the income: "))
    except ValueError:
        print("Not an integer")
        trackincome()


def trackdate():
    try:
        date=input("enter the date (DD-MM-YY): ")
        date_object = datetime.datetime.strptime(date, "%d-%m-%Y").date()
    except:
        print("Invalid Date Format")
        trackdate()




main()

