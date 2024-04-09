# Unit 1/2 Activity
# Author: Kendrick Phu
# April 9, 2024

user_answer = input("Do you like watching Formula 1?").lower().strip("!?.,")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input("Seriously, do you like  ice cream?").lower().strip("!?.,")

if user_answer in ["yes", "yeah"]:
    print("Amazing. I also loveee Formula 1.")
elif user_answer in ["no", "nah"]:
    print("How could you not like FOrmula 1?")