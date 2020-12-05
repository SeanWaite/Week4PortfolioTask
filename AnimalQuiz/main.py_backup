import random    # Import random library for additional functions
import Insect.insect as i    # Import insect class
import Mammal.mammal as m    # Import mammal class

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
    insect_string = i.Insect(animal, eye_correct, leg_correct, wings_correct)

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
#   print(repr(insect_string))
#   print(insect_string)
else:
    mammal_string = m.Mammal(animal, eye_correct, leg_correct, sound_correct)

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
#   print(repr(mammal_string))
#   print(mammal_string)

print("\nWell done, thanks for playing!")
