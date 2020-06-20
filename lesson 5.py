class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        return "Firefooooooooox!"

fox = Animal("fox")

print("Enter multi-shine Melee bastard: " + fox.species)

print(fox.speak())
