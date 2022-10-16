# On every year that is evenly divisible by 4 except
# every year that is evenly divisible by 100 unless
# the year is also evenly divisible by 400

year = int(input("What year would you like to check for leap year-ish-ness? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Sorry, not a leap year.")
    else:
        print("Leap year!")
else:
    print("Sorry, not a leap year.")