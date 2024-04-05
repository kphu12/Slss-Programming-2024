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