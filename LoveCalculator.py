print("Welcome to the Love Calculator")
your_name = input("What is your name? ").lower()
her_name = input("What is your love interest's name? ").lower()
combined_names = your_name + her_name
true_score = combined_names.count("t")
true_score += combined_names.count("r")
true_score += combined_names.count("u")
true_score += combined_names.count("e")
love_score = combined_names.count("l")
love_score += combined_names.count("o")
love_score += combined_names.count("v")
love_score += combined_names.count("e")
print(f"Your love score is {true_score}{love_score}!")
combined_score = int(true_score * 10 + love_score)
if combined_score < 10 or combined_score > 90:
    print("You go together like coke and mentos!")
elif combined_score >= 40 and combined_score <= 50:
    print("You are alright together.")
