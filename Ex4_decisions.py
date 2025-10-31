# -------------------------------------------
# Exercise 4: Decision-Making Program
# -------------------------------------------
# In this exercise, you will write a program that makes decisions based on user input.
# You will practice combining Boolean logic with conditional statements.
#
# Goals:
# - Ask the user for input
# - Use conditions to decide what to do
# - Print messages based on the conditions
# - Test your program with different inputs

# -------------------------------------------
# Task 1: Simple decision
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Ask the user to enter a number.
# Decide something about the number using an if statement.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message for True condition")

# TODO:
# 1. Ask the user to type a number and store it in a variable.
# 2. Use an if statement to check something about the number.
# 3. Print a message if the condition is True.

# Write your code below:
userNumber = int(input("write a number!  "))
if userNumber <=10:
    print("You are not eligible!")


# -------------------------------------------
# Task 2: Add else
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# Sometimes we need to print a different message if the condition is False.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message if True")
# else:
#     print("Message if False")

# TODO:
# 1. Add an else statement to your code from Step 1.
# 2. Print a different message if the number does not meet your condition.

# Write your code below:

else:
    print("Welcome You are eligible!")
# -------------------------------------------
# Task 3: Multiple conditions
# -------------------------------------------
# Note: Read all of the instructions below first before starting!

# You can check more than one condition using elif or Boolean operators.

# Example of syntax (no answer given):
# if condition1:
#     print("Message 1")
# elif condition2:
#     print("Message 2")
# else:
#     print("Message 3")

# TODO:
# 1. Extend your program to check multiple conditions.
# 2. Print different messages for each case.
# 3. Test your program with different inputs to see all possible messages.

# Write your code below:

doorNumber = int(input("Write your door number please! "))

if doorNumber < 123:
    print("You live in Theatre Street")
elif doorNumber >= 123 and doorNumber <= 153:
    print("You live in Susame Street")
else:
    print("You live out of Airport Area")
# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed decision-making program exercise"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1:
# Ask the user for a number and a word.
# Use conditions to print a message only if the number is greater than a value
# AND the word matches a stored word.

# Extension 2:
# Ask the user for a number.
# Print different messages depending on:
# - number is positive
# - number is zero
# - number is negative

# Extension 3 (more challenging):
# Create a small quiz:
# - Ask the user a multiple-choice question.
# - Check their answer and print "Correct!" or "Try again!".
# - Add another condition to give a special message if the answer is partially correct.

# Write your extension code below:
question = int(input("How many region does Turkiye have? "))

if question ==7:
    print("Well done! That is True")
elif question >1 and question <7:
    print("Not exactly, but you are close!")
else:
    print("OH! no! Please try again")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed extension activities"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------
