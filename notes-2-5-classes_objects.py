# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and fuctions together
#   - Objects are the ACTUAL reppresentation of the classes

# Create a Pokemon class; this represents a Pokemon
class Pokemon: # use a capital letter for class name
    def __init__(self):
        """A special method (funtion) called the 
        Constructor. Contains all the properties/variables 
        that describe a Pokemon."""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"


        print("A new Pokemon is born!")

# Create two Pokemon using our class
# Make one Pokemon that is Pikachu
pokemon_one = Pokemon()

# Change some properties in pokemon_one
#    Change its name
print(pokemon_one.name)         # ""
pokemon_one.name = "Pikachu"
print(pokemon_one.name)         # "Pikachu"

pokemon_one.id = 25
pokemon_one.type = "Electric"

print(pokemon_one.id)
print(pokemon_one.type)

# Make one Pokemon of your choice
#   - you can make Squirtle

pokemon_two = Pokemon()
print(pokemon_two.name)         # ""
pokemon_two.name = "Squirtle"
print(pokemon_two.name)         # "Squirtke"

pokemon_two.id = 4
pokemon_two.type = "Water"
pokemon_two.weight = "1'08''"
pokemon_two.height = "19.8 lbs"

print(pokemon_two.id)
print(pokemon_two.type)
print(pokemon_two.weight)
print(pokemon_two.height)
