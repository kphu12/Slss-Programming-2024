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
        self.actual_cry = "Rooooooooooar!"


        print("A new Pokemon is born!")
    
    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
            - string representing the sound it makes"""
        return f"{self.name} says, \"{self.actual_cry}\"!"

    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon
        
        Params:
            - food: what food you feed it

        Return:
            - what it says after eating it"""
        if food.lower() == "berry":
            return f"{self.name} at the berry and says, \"YUM!\""
        elif food.lower() == "potion":
            return f"{self.name} consued the potion and feels better"
        else:
            return f"{self.name} batted the {food} away"

# Create a new child class of Pokemon
class Pikachu(Pokemon):
    def __init__(self, name="Pikachu"):
        # Call constructor of parent class
        super().__init__()

        # Assign the default value to properties
        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikachu"

    def thundershock(self, defender: Pokemon) -> str:
        """Simulate a thundershock attack against
        anoter Pokemon.

        Params:
            - defender: defending Pokemon
        
        Returns:
            str representing result of attack.
        """
        response = f"{self.name} used thundershock on {defender.name}!"

        if defender.type.lower() in ["water", "flying"]:
            response = response + " It was super effective."
        
        return response
    

# Create a new child-class of pokemon for the type of your choice
# If you don't know any pokemon, use this: https://pokemondb.net/pokedex/national
#   - create a new child class
#   - create a constructor and set the default values for its properties
#       - i.e. its name, id, type, etc.
#   - create a new method for its attack

class Shuppet(Pokemon):
    def __init__(self, name= "Shuppet"):
        self.name = name
        self.id = 353
        self.actual_cry = "Blarrgeeeblargblarg"

    def shadow_ball(self, defender: Pokemon) -> str:
        pass

     # Assign the default values to properties

    def shadow_ball(self, defender: Pokemon) -> str:
        """Ghost type attack"""
        response = f"{self.name} used cursed body on {defender.name}."

        if defender.type.lower() in ["psychic", "ghost"]:
            response = response + " It was super effective!"
        elif defender.type.lower() in ["dark"]:
            response = response + " It was not very effective."

        return response

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
pokemon_two.weight = "1\'08\""
pokemon_two.height = "19.8 lbs"

print(pokemon_two.id)
print(pokemon_two.type)
print(pokemon_two.weight)
print(pokemon_two.height)

pokemon_one.actual_cry = "Pikachu"
pokemon_two.actual_cry = "Grraaaauuhhhh"

print(pokemon_one.cry())
print(pokemon_two.cry())

# Test the eat method
print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion"))
print(pokemon_one.eat("posion"))

pikachu_one = Pikachu()         #Pikachu
pikachu_two = Pikachu("Speedy") #Speedy

print(pikachu_one.name)
print(pikachu_two.name)
print(pikachu_one.cry())
print(pikachu_two.eat("potion"))

print(pikachu_one.thundershock(pokemon_one))
print(pikachu_two.thundershock(pokemon_two))