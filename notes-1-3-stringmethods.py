# Methods (Strings)
# Author: Kendrick
# 22 February 2024

# terminal, python3
# quit to get out of it

# Ask the user what is the weather like
weather = input("What's the weather like?")

# If they reply rainy
    # Bring an umbrella
if weather.lower().strip("!.?, ") == "rainy":
    print("You'll need an umbrella!")
else:
    print(f"Sorry, I don't understnad {weather}")