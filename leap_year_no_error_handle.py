# Leap year program

val = input("Enter a year to check if it's a leap year: ")
if val % 4 == 0:
    if val % 100 == 0:
        if val % 400 == 0:
            print("The given year is a leap year!")
        else:
            print("The given year is not a leap year.")
    else:
        print("The given year is a leap year!")
else:
    print("The given year is not a leap year.")