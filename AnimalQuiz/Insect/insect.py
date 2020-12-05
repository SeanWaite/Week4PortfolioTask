import Animal.animal as a


# Insect class is a child of Animal and adds a feature of insects
class Insect(a.Animal):
    def __init__(self, species, eyes, legs, wings):
        super().__init__(species, eyes, legs)
        self.wings = wings

    # Below method gives the correct answer
    def print_insect(self):
        print("The insect is a " + self.species + ".", "It has " + self.eyes +
              " eyes, " + self.legs + " legs and " + self.wings + " wings.\n")

    # Return answer given
    def insect_return_answer(self):
        return self.wings

    # Set back to correct answer
    def insect_set_answer(self, wings):
        self.wings = wings

    def __str__(self):
        return "\nPassed in values\nInsect is: " + self.species + \
               "\nEyes: " + self.eyes + \
               "\nLegs: " + self.legs + \
               "\nWings: " + self.wings

    def __repr__(self):
        return 'Insect(species=%s, eyes=%s, legs=%s, wings=%s)' % \
                      (self.species, self.eyes, self.legs, self.wings)
