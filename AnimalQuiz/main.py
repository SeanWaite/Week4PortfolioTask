import random    # Import random library for additional functions
import csv    # Used to open and read csv files
import itertools
import Insect.insect as i    # Import insect class
import Mammal.mammal as m    # Import mammal class

# Open quiz_data.csv
with open('quiz_data.csv') as quiz_data:
    lines_numbers = sum(1 for line in quiz_data)
    random_line = random.randint(1, lines_numbers - 1)
    quiz_data.seek(0)
    chosen_line = next(csv.DictReader(itertools.islice(quiz_data,
                                                       random_line,
                                                       None),
                                      fieldnames=("type",
                                                  "name",
                                                  "eyes",
                                                  "legs",
                                                  "bonus_question",
                                                  "bonus_answer")))

# Start of main process
print("Welcome to animal facts\nPlease answer the below question:\n")

# Retrieve correct answers
animal_type = chosen_line.get("type")
animal = chosen_line.get("name")
eye_correct = chosen_line.get("eyes")
leg_correct = chosen_line.get("legs")
bonus_question = chosen_line.get("bonus_question")
bonus_correct = chosen_line.get("bonus_answer")

# Ask for the answers to questions
eye_answer = input("How many eyes does a " + animal + " have?\n")
leg_answer = input("How many legs does a " + animal + " have?\n")

# Based on animal ask certain bonus questions
if animal_type == 'Insect':
    insect_string = i.Insect(animal, eye_correct, leg_correct, bonus_correct)

    if eye_answer == eye_correct and leg_answer == leg_correct:
        print('\nCorrect Answers\n')
    else:
        print('\nSorry that is incorrect\n')

    # Print answers from parent
    insect_string.print_animal()

    # Ask extra question
    insect_string.insect_set_answer(input(f"{bonus_question}"))

    if bonus_correct == insect_string.insect_return_answer():
        print('\nCorrect Answer\n')
    else:
        print('Sorry that is incorrect')
        # If answer was wrong need to set back to correct answer
        insect_string.insect_set_answer(bonus_correct)

    # Print answers from child
    insect_string.print_insect()

#   Uncomment for debugging
#   print(repr(insect_string))
#   print(insect_string)
else:
    mammal_string = m.Mammal(animal, eye_correct, leg_correct, bonus_correct)

    if eye_answer == eye_correct and leg_answer == leg_correct:
        print('\nCorrect Answers\n')
    else:
        print('Sorry that is incorrect')

    # Print answers from parent
    mammal_string.print_animal()

    # Ask extra question
    mammal_string.mammal_set_answer(input(f"{bonus_question}"))

    if bonus_correct.upper() == mammal_string.mammal_return_answer().upper():
        print('\nCorrect Answer\n')
    else:
        print('\nSorry that is incorrect\n')
        # If answer was wrong need to set back to correct answer
        mammal_string.mammal_set_answer(bonus_correct)

    # Ask answers from child
    mammal_string.print_mammal()

#   Uncomment for debugging
#   print(repr(mammal_string))
#   print(mammal_string)

print("\nWell done, thanks for playing!")
