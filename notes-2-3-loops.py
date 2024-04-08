# Loops and Iteration
# Author: Kendrick Phu
# 5 April 2024

# Print "something" 10 times
for _ in range(10):
    print("something")

# Create a grocery list
# Do something for each item in the list
grocery_list = [
    "blueberry muffins",
    "potato chips",
    "aluminium foil",
    "oramge juice",
    "RTX 4070 Super",
    "cereal"
]

# for every item in the list:
#   *{grocery item}
#   *{grocery item}
#   *{grocery item}
for item in grocery_list:
    # skip the rest of the list
    # if we get to rtx 4070
    if item.lower() == "rtx 4070 super":
        print("Mr. Ubial can't buy a  4070!")
        break # STOP LOOPING
    print(f"* {item}")

# Cn you count using a for loop?
# Use a for loop to count to 100
for i in range(100):
    print(i + 1)

# This loops repeats indefinitely

# while True:
#     print("This is an infinite loop")

# while loops are useful for input validation
# Ask the user if they like ice cream
#   If they don't answer yes or no
#       Repeat the question

user_answer = input("Do you like ice cream?").lower().strip("!?.,")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input("Seriously, do you like  ice cream?").lower().strip("!?.,")

if user_answer in ["yes", "yeah"]:
    print("Nice. I LOOOOVE ice cream, too.")
elif user_answer in ["no", "nah"]:
    print("How could you not like ice cream?")