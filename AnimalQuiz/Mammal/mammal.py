import Animal.animal as a


# Mammal class is a child of Animal and adds the sound some make
class Mammal(a.Animal):
    def __init__(self, species, eyes, legs, sound):
        super().__init__(species, eyes, legs)
        self.sound = sound

    # Below method gives the correct answer
    def print_mammal(self):
        print("The mammal is a " + self.species + ".",
              "It has " + self.eyes +
              " eyes, " + self.legs +
              " legs and makes a " + self.sound + " sound.\n")

    # Return answer given
    def mammal_return_answer(self):
        return self.sound

    # Set back to correct answer
    def mammal_set_answer(self, sound):
        self.sound = sound

    def __str__(self):
        return "\nPassed in values\nMammal is: " + self.species + \
               "\nEyes: " + self.eyes + \
               "\nLegs: " + self.legs + \
               "\nSound: " + self.sound

    def __repr__(self):
        return 'Mammal(species=%s, eyes=%s, legs=%s, sound=%s)' % \
                      (self.species, self.eyes, self.legs, self.sound)
