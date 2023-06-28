finish=False
while finish == False:
    choice = input ("hours or minutes?:")
    if choice == ("hours"):
        value = input("hours:")
        result = int(value)*60
        print("minutes:",result)
        finish = True
    elif choice== ("minutes"):
        value = input("minutes:")
        result = int(value)/60
        print("hours:",result)
        finish = True
    else:
        print("please type either 'hours' or 'minutes'.")
        