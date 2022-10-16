print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo? Y or N only please. ").upper()[:1]
    if wants_photo =="Y":
        bill = bill + 3
        print(f"Your new ticket price is ${bill}")
else:
    print("Sorry shorty, you can't ride the rollercoaster.")
