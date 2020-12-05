# Animal class is a the parent. All animals in the list share these features
class Animal():
    def __init__(self, species, eyes, legs):
        self.species = species
        self.eyes = eyes
        self.legs = legs

    # Below method gives the correct answer
    def print_animal(self):
        print("The animal is a " + self.species + ".", "It has " +
              self.eyes + " eyes and " + self.legs + " legs.\n")

    def __str__(self):
        return "Passed in values\nAnimal is: " + self.species + \
               "\nEyes: " + str(self.eyes) + \
               "\nLegs: " + str(self.legs)

    def __repr__(self):
        return 'Animal(species=%s, eyes=%s, legs=%s)' % \
                      (self.species, self.eyes, self.legs)
