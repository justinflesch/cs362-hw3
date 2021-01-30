# Leap year program WITH error handling

val = str(input("Enter a year to check if it's a leap year: "))
if isinstance(val, int):
    if val >= 0:
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
    else:
        print("Seems like you gave a negative number.")
else:
    print("That's not a number, or it's a negative number!")