#Twoim zadaniem jest napisanie i przetestowanie funkcji, która wymaga jednego argumentu (roku)
# i zwraca wartość True jeżeli rok jest przestępny, lub False jeśli nie jest.

def leapYear(year):

    if year % 4 == 0:
        print(f"{year} is a leap year - True")

    else:
        print(f"{year} isn't a leap year - False")

leapYear(1900)
leapYear(2000)
leapYear(2016)
leapYear(1987)
