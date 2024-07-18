import datetime



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
        while True:
            try:
                expense=int(input("please enter the amount of expense: "))
                break
            except ValueError:
                print("Not an integer")
                pass

    elif track.upper() == "I":
        # while True:
        #     try:
        #         income=int(input("please enter the amount of income: "))
        #         date=input("please enter the date (DD-MM-YY): ")
        #         date_object = datetime.datetime.strptime(date, "%d-%m-%y").date()
        #     except ValueError:
        #         print("Not an integer")
        #         pass

        trackincome()
        trackdate()
                
                
                
            
    else:
        record()


def trackincome():
    try:
        income=int(input("enter the income: "))
    except ValueError:
        trackincome()


def trackdate():
    try:
        date=input("enter the date: ")
    except ValueError:
        trackdate()
    




# def balance():



main()