year=int(input("Which year do you want to check "))
if year%4!=0:
    print("The year is not leap year")
else:
    if year%100==0:
        if year%400!=0:
            print("The year is not leap year")
        else:
            print("The year is a leap year")
    else:
        print("The year is leap year")