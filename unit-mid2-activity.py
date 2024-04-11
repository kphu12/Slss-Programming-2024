# Unit 1/2 Activity
# Author: Kendrick Phu
# April 9, 2024

user_answer = input("Do you like watching Formula 1?").lower().strip("!?.,")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input("Seriously, do you like Formula 1?").lower().strip("!?.,")

if user_answer in ["yes", "yeah"]:
    print("Amazing. I also loveee Formula 1.")
elif user_answer in ["no", "nah"]:
    print("How could you not like Formula 1?")

def favourite_team(team):
    if team.lower().strip("!?.,") == "ferrari":
        return"Forza Ferrari!!"
    if team.lower().strip("!?.,") == "red bull":
        return"The domination is crazy."
    if team.lower().strip("!?.,") == "mercedes":
        return"Downfall needs to be studied"
    if team.lower().strip("!?.,") == "aston martin":
        return"Fernando Alonsooo"
    if team.lower().strip("!?.,") == "mclaren":
        return"Slowly climbing the ranks"
    if team.lower().strip("!?.,") == "alpine":
        return"Must be a sad year"
    if team.lower().strip("!?.,") == "haas":
        return"Lowkey cooking this year!!"
    if team.lower().strip("!?.,") == "racing bulls":
        return"lovely driver lineup"
    if team.lower().strip("!?.,") == "williams":
        return"not a great year again"
    if team.lower().strip("!?.,") == "Stake":
        return"Need to fix your pitstops"
    

user_answer = input("What's your favourite team?").lower().strip("!?.,")
print(favourite_team(user_answer))

