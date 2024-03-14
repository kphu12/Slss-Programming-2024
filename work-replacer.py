# Emoji replacer
# Author: Kendrick
# 27 February 2024

# Create a function called replacer
#   Accepts a string
#   Replace all 100 with 💯
#   Replace all noodles with 🍜
#   Return the result
def translate(usr_input) -> str:
    # This is where your code goes
    # Delete the pass and put in your own code
    return usr_input.replace("100", "💯").replace("noodles", "🍜")

def main():
    # Get the user's input
    usr_input = input()
    #   user's input
    print(translate(usr_input))

# Test cases
print(translate("Get to 100!"))
print(translate("I like noodes."))    
print(translate("I love 100 noodles."))
main()
