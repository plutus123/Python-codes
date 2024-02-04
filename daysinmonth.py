def is_leap(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 == 0:
            if year % 400 != 0:
                return False
            else:
                return True
        else:
            return True
def days_in_month(years,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
   
    if is_leap(years) and month==2:
        return 29
    return month_days[month-1]
year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
days=days_in_month(year,month)
print(days)