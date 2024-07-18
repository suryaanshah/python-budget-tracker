def init():
    todo=input("What do want to do?\n 1. record a statement (R)\n 2. show the balance-sheet (B)\n 3. tutorial (T)\nYour Answer: ")
    if todo.upper()=='R':
        record()

    # elif todo.upper()=='B':
    #     balance()
    # elif todo.upper()=='T':
    #     tutorial()

    else:
        init()


def record():
    track=input("Is it an expense (E) or an income (I)? ")
    if track.upper() == "E":
        while True:
            try:
                expense=int(input("please enter the amount of expense: "))
                date=input("Please enter the date: ")
                break
            except ValueError:
                print("Not a positive integer")
                pass

    elif track == "I":
        while True:
            try:
                income=int(input("please enter the amount of income: "))
                date= input("Please enter the date: ")
                break
            except ValueError:
                pass
    else:
        record()

init()