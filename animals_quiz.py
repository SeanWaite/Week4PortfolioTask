import random    # Import random library for additional functions


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


# Insect class is a child of Animal and adds a feature of insects
class Insect(Animal):
    def __init__(self, species, eyes, legs, wings):
        super().__init__(species, eyes, legs)
        self.wings = wings

    # Below method gives the correct answer
    def print_insect(self):
        print("The insect is a " + self.species + ".", "It has " + self.eyes +
              " eyes, " + self.legs + " legs and " + self.wings + " wings.\n")

    # Bonus question to be asked
    def insect_bonus_question(self):
        self.wings = input("How many wings does a " + self.species + " have?\n")

    # Return answer given
    def insect_bonus_answer(self):
        return self.wings

    # Set back to correct answer
    def insect_right_answer(self, wings):
        self.wings = wings

    def __str__(self):
        return "\nPassed in values\nInsect is: " + self.species + \
               "\nEyes: " + self.eyes + \
               "\nLegs: " + self.legs + \
               "\nWings: " + self.wings

    def __repr__(self):
        return 'Insect(species=%s, eyes=%s, legs=%s, wings=%s)' % \
                      (self.species, self.eyes, self.legs, self.wings)


# Mammal class is a child of Animal and adds the sound some make
class Mammal(Animal):
    def __init__(self, species, eyes, legs, sound):
        super().__init__(species, eyes, legs)
        self.sound = sound

    # Below method gives the correct answer
    def print_mammal(self):
        print("The mammal is a " + self.species + ".",
              "It has " + self.eyes +
              " eyes, " + self.legs +
              " legs and makes a " + self.sound + " sound.\n")

    # Bonus question to be asked
    def mammal_bonus_question(self):
        self.sound = input("What sound does a " + self.species + " make?\n")

    # Return answer given
    def mammal_bonus_answer(self):
        return self.sound

    # Set back to correct answer
    def mammal_right_answer(self, sound):
        self.sound = sound

    def __str__(self):
        return "\nPassed in values\nMammal is: " + self.species + \
               "\nEyes: " + self.eyes + \
               "\nLegs: " + self.legs + \
               "\nSound: " + self.sound

    def __repr__(self):
        return 'Mammal(species=%s, eyes=%s, legs=%s, sound=%s)' % \
                      (self.species, self.eyes, self.legs, self.sound)


# Start of main process
print("Welcome to animal facts\nPlease answer the below question:\n")

# Lists of animals and corret answers
animals = ["Cat", "Dog", "Kangaroo", "Bee", "Dragonfly", "Dung Beetle"]
eye_list = ["2", "2", "2", "5", "5", "4"]
leg_list = ["4", "4", "2", "6", "6", "6"]
sound_list = ["meow", "woof", "chortle", "", "", ""]
wings_list = ["", "", "", "4", "4", "4"]

# Randomly select the animal for be asked about
animal = random.choice(["Cat", "Dog", "Kangaroo", "Bee", "Dragonfly", "Dung Beetle"])

# Retrieve correct answers
location = animals.index(animal)
eye_correct = eye_list[location]
leg_correct = leg_list[location]
sound_correct = sound_list[location]
wings_correct = wings_list[location]

# Ask for the answers to questions
eye_answer = input("How many eyes does a " + animal + " have?\n")
leg_answer = input("How many legs does a " + animal + " have?\n")

# Based on animal ask certain bonus questions
if location >= 3:
    insect_string = Insect(animal, eye_correct, leg_correct, wings_correct)

    if eye_answer == eye_correct and leg_answer == leg_correct:
        print('\nCorrect Answers\n')
    else:
        print('\nSorry that is incorrect\n')

    # Print answers from parent
    insect_string.print_animal()

    # Ask extra question
    insect_string.insect_bonus_question()

    if wings_correct == insect_string.insect_bonus_answer():
        print('\nCorrect Answer\n')
    else:
        print('Sorry that is incorrect')
        # If answer was wrong need to set back to correct answer
        insect_string.insect_right_answer(wings_correct)

    # Print answers from child
    insect_string.print_insect()

#   Uncomment for debugging
    print(repr(insect_string))
#   print(insect_string)
else:
    mammal_string = Mammal(animal, eye_correct, leg_correct, sound_correct)

    if eye_answer == eye_correct and leg_answer == leg_correct:
        print('\nCorrect Answers\n')
    else:
        print('Sorry that is incorrect')

    # Print answers from parent
    mammal_string.print_animal()

    # Ask extra question
    mammal_string.mammal_bonus_question()

    if sound_correct.upper() == mammal_string.mammal_bonus_answer().upper():
        print('\nCorrect Answer\n')
        mammal_string.mammal_right_answer(sound_correct)
    else:
        print('\nSorry that is incorrect\n')
        # If answer was wrong need to set back to correct answer
        mammal_string.mammal_right_answer(sound_correct)

    # Ask answers from child
    mammal_string.print_mammal()

#   Uncomment for debugging
    print(repr(mammal_string))
#   print(mammal_string)

print("\nWell done, thanks for playing!")
