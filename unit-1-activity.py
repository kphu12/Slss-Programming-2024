# Unit 1 Activity
# Author: Kendrick Phu
# March 4, 2024




print("Hello user")
print("What's your name?")
name = input()
print (f"Hi {name}")



semester = input("What are your thoughts on the 2023 F1 season?\na)Very Good\nb)Good\nc)Decent\nd)Bad\n")

if semester=="a":
    print("Max Verstappen fan?")
elif semester=="b":
    print("Reasonable, was still a bit of action.")
elif semester=="c":
    print("Midfield team supporter?")
elif semester=="d":
    print("Not a Max Verstappen fan?")
    exit()

def formula_race(team):
    return team

team = input("What is the best formula one team of all time?")

if team.lower().strip("!.?, ") == "mercedes":
    print("Good choice!")

if team.lower().strip("!.?, ") == "mclaren":
    print("Might be your year soon!")

if team.lower().strip("!.?, ") == "ferrari":
    print("Tough day nowadays!")

if team.lower().strip("!.?, ") == "redbull":
    print("Must be loving life right now!!")

if team.lower().strip("!.?, ") == "alpine":
    print("2024 season not looking too great")

if team.lower().strip("!.?, ") == "aston martin":
    print("Good choice!")

if team.lower().strip("!.?, ") == "haas":
    print("No more best principal, Guenther Steiner!!")

if team.lower().strip("!.?, ") == "stake":
    print("Weirdest name and livery on the grid!")

if team.lower().strip("!.?, ") == "visa cash app racing bulls":
    print("Most awkard driver lineup.")

if team.lower().strip("!.?, ") == "williams":
    print("Reasonable,")