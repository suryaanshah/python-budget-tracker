def init():
    todo=input("What do want to see?\n 1. record a statement (R)\n 2. show the balance-sheet (B)\n 3. tutorial (T)\nYour Answer: ")
    if todo.upper()=='R':
        record()

   # elif todo.upper()=='B':
    #    balance()
   # elif todo.upper()=='T':
    #    tutorial()

    else:
        init()


def record():
    track=input("Is it an expense (E) or an income (I)? ");
    if track == "E":
        expense=int(input("please enter the amount of expense: "))
        date=input("Please enter the date: ")

    elif track == "I":
        income=int(input("please enter the amount of income: "))
        date= input("Please enter the date: ")
    else:
        record()

init()