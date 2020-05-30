# Twoim zadaniem jest napisanie i przetestowanie funkcji,
# (rok, miesiąc, oraz dzień miesiąca) i zwraca odpowiedni dzień roku
# lub wartość None jeśli którykolwiek z argumentów jest nieprawidłowy.

def yearLeap(year):
    if year % 4 == 0:
        print(f"{year} is a leap year.")

    else:
        print(f"{year} isn't a leap year.")

def daysMonth(month):

    listDays30 = [4, 6, 9, 11]
    listDays31 = [1, 3, 5, 7, 8, 10, 12]

    if year % 4 == 0:
        if month == 2:
            print(f'Month {month} has 29 days')
        elif month in listDays30:
            print(f'Month {month} has 30 days')
        elif month in listDays31:
            print(f'Month {month} has 31 days')

    else:
        if month == 2:
            print(f'Month {month} has 28 days')
        elif month in listDays30:
            print(f'Month {month} has 30 days')
        elif month in listDays31:
            print(f'Month {month} has 31 days')

def dateUser(year, month, day):
    if day < 10 and month < 10:
        print(f'Date: {year}.0{month}.0{day}')
    elif day < 10:
        print(f'Date: {year}.{month}.0{day}')
    elif month < 10:
        print(f'Date: {year}.0{month}.{day}')
    else:
        print(f'Date: {year}.{month}.{day}')

print('')

year = int(input('Enter the year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

yearLeap(year)
daysMonth(month)
dateUser(year, month, day)
