print("Welcome to Pizza Pizza!")
size = input("What size pizza would you like? S/M/L? ").upper()[:1]
pepperoni = input("Would you like pepperoni on that? Y/N? ").upper()[:1]
cheese = input("Would you like extra cheese? Y/N? ").upper()[:1]
price = 0
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Invalid size. Please try again.")
if pepperoni == "Y":
    if price == 15:
        price += 2
    else:
        price += 3
if cheese == "Y":
    price += 1
print(f"Your final price is ${price}.")