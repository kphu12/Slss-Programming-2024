# Deep Thought
# Author: Kendrick Phu
# 22 February 2024


# make a bot that says yes only to different variations of 42

# ask the prompt
# if statements
# type response for each solution under each if statements

#asking promt
foo = input("What is the answer of life, the universe, and everything?")

# correct answers
if foo == "42":
    print("yes")

elif foo == "forty two":
    print("yes")

elif foo == "forty-two":
    print("yes")

elif foo == "Forty-two":
    print("yes")

elif foo == "Forty_two":
    print("yes")
# wrong answer
else:
    print("no")