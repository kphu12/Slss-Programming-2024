# McDoBot
# Author: Kendrick Phu
# 22 February 2024

# Ask the user if they want fries with their meal
fries = input("Would you like frise with your meal? (Yes/No)")

# If they reply rainy
    # Bring an umbrella
if fries.lower().strip("!.?, ") == "yes":
    print("Here's your meal with fries, sir!")

elif fries.lower().strip("!,.? ") == "no":
    print("Here's your meal without fries, sir!")
else:
    print(f"Sorry, I don't understand {fries}")